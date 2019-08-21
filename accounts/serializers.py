from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password',]


class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = "email"


