from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, min_length=4)
    password = serializers.CharField(min_length=4)
