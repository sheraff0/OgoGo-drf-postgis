from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from contrib.users.models import OTP
from contrib.utils.verify import get_verification_code
from .backends import EmailOrUsernameModelBackend as backend


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        token, _ = Token.objects.get_or_create(user=user)
        attrs["token"] = token.key
        return attrs


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    code = serializers.CharField(write_only=True)
    phone = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birth_date = serializers.DateField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, value):
        email = value.lower()
        if user := backend.obtain_user(email, key="email"):
            raise ValidationError(detail="Email already exists!", code=status.HTTP_400_BAD_REQUEST)
        return email

    def validate_username(self, value):
        if backend.obtain_user(value):
            raise ValidationError(detail="Username already exists!", code=status.HTTP_400_BAD_REQUEST)
        return value

    def validate(self, attrs):
        username, email = map(attrs.get, ("username", "email"))
        code, password, password2  = map(attrs.pop, ("code", "password", "password2"))

        if password != password2:
            raise ValidationError(detail="Password fields do not match!", code=status.HTTP_400_BAD_REQUEST)

        try:
            OTP.objects.get(email=email, is_verified=True, code=code)
        except:
            raise ValidationError(detail="Email verification failed!", code=status.HTTP_400_BAD_REQUEST)

        user = backend.User(**attrs)
        user.set_password(password)
        user.save()
        return user


class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

    @transaction.atomic
    def validate_email(self, value):
        email = value.lower()
        otp, _ = OTP.objects.update_or_create(
            email=email, defaults=dict(
                is_verified=False,
                code=get_verification_code(),
                attempts=3,
                last_update=datetime.now()
            )
        )
        subject = "ОГО Go! - код подтверждения"
        message = f"""Код подтверждения: {otp.code}"""
        html_message = f"""Код подтверждения:
            <span style="font-size: larger; font-weight: 900; color: #ff5a0c">{otp.code}</span>"""
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email], html_message=html_message)
        except:
            raise ValidationError(detail="Unable to send verification email!", code=status.HTTP_503_SERVICE_UNAVAILABLE)


class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    code = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    created = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        email, code = map(attrs.get, ("email", "code"))
        email = email.lower()
        otp = get_object_or_404(OTP, email=email)
        if otp.expired:
            otp.delete()
            raise ValidationError(detail="Code expired!", code=status.HTTP_400_BAD_REQUEST)
        if not (otp.attempts > 0):
            raise ValidationError(detail="Too many attempts!", code=status.HTTP_400_BAD_REQUEST)
        try:
            assert otp.verify(code)
        except:
            raise ValidationError(detail="Wrong code!", code=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            user, created = backend.User.objects.update_or_create(email=email)
            if created:
                user.username = f"{email}-{int(datetime.now().timestamp())}"
                user.set_password(settings.DEFAULT_PASSWORD)
            user.save()
            otp.delete()
            token, _ = Token.objects.get_or_create(user=user)
            attrs.update({
                "token": token.key,
                "created": created
            }) 
            return attrs
