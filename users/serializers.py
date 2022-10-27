from django.core.validators import RegexValidator

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


PASSWORD_REGEX = RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})')


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password1 = serializers.CharField(max_length=30, validators=[PASSWORD_REGEX])
    password2 = serializers.CharField(max_length=30, validators=[PASSWORD_REGEX])

    def validate(self, attrs):
        password1 = attrs.get('password1', None)
        password2 = attrs.get('password2', None)

        if password1 != password2:
            raise ValidationError({"detail": "Your passwords didn't match."}, code=400)

        return attrs


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=30)