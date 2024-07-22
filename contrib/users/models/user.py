"""
Custom User model and manager
"""
from uuid import uuid4

from rest_framework.authtoken.models import Token
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from contrib.common.models import UUIDModel


class CustomBaseUserManager(BaseUserManager):
    """
    Custom user model manager where phone is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, **extra_fields):
        """
        Create and save a User with the given phone and set passwordless.
        """
        user: BaseUserManager = self.model(**extra_fields)
        user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone and password.
        """

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        Token.objects.get_or_create(user=user)
        return user


class User(AbstractBaseUser, PermissionsMixin, UUIDModel):
    """
    User model
    """
    username = models.CharField(unique=True, max_length=70, blank=True, null=True)
    email = models.EmailField('email', unique=True, null=True)
    phone = models.CharField(unique=True, max_length=70, blank=True, null=True)
    first_name = models.CharField('first name', max_length=70)
    last_name = models.CharField('last name', max_length=70)
    birth_date = models.DateField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField('active', default=True)

    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = CustomBaseUserManager()

    @property
    def token(self):
        try:
            return self.auth_token
        except:
            Token.objects.get_or_create(user=self)
        return self.auth_token

    def __str__(self):
        """
        Object name
        """
        return f"{self.username} ({self.email})"

    class Meta:
        """
        It's persisted model
        """
        verbose_name = 'user'
        verbose_name_plural = 'users'
