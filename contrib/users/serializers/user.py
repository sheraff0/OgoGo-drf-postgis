from django.db.models import Q
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from contrib.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'avatar', 'birth_date', 'email', 'phone', 'password']
        extra_kwargs = {'email': {'read_only': True}, 'password': {'write_only': True}}
        depth = 0

    def validate_username(self, value):
        try:
            assert value
            user_id = self.context["user"].pk
            assert not User.objects.filter(~Q(pk=user_id), username=value).exists()
        except:
            raise ValidationError(detail="Cannot change username!", code=status.HTTP_400_BAD_REQUEST)
        return value

    def update(self, instance, validated_data):
        """ Updating User """
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            if key == 'avatar' and instance.avatar:
                instance.avatar.delete()
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class UserWithTokenSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'avatar', 'birth_date', 'email', 'token']
