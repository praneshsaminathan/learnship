from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)
        if user is None:

            raise serializers.ValidationError({'username': _('User with given email and password does not exists')})

        token = RefreshToken.for_user(user)
        jwt_token = str(token.access_token)
        update_last_login(None, user)

        return {
            'email':user.email,
            'token': jwt_token
        }
