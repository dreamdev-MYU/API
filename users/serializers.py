from django.contrib.auth.models import User
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, min_length=5)
    password = serializers.CharField(max_length=8, min_length=4)

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=8, min_length=4)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')

    def save(self):
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        email = self.validated_data['email']

        if confirm_password != password:
            raise serializers.ValidationError("Passwords don't match!!!")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists in the database")

        user = User.objects.create_user(username=self.validated_data['username'], email=email, password=password)
        return user
