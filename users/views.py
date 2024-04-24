from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, RegisterSerializer

class LoginApiView(APIView):
    def post(self, request):
        request_data = request.data
        serializer = LoginSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**request_data)

        if user is None:
            result = {
                "status": "False",
                "message": "User not found"
            }
            return Response(result)
        else:
            refresh = RefreshToken.for_user(user)

            data = {
                "Refresh": str(refresh),
                "Access": str(refresh.access_token)
            }
            return Response(data)

class RegisterApiView(APIView):
    def post(self, request):
        request_data = request.data
        serializer = RegisterSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        data = {
            "status": True,
            "message": f"{user.username} is Registered"
        }
        return Response(data)
