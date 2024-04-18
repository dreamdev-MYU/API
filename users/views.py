from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken



class LoginApiView(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(username=serializer.data['username'], password = serializer.data['password'])

        if user is None:
            data = {
                "status":False,
                "massage":"User not found"
            }

            return Response(data)
        refresh = RefreshToken.for_user(user)

        data = {
            'refresh':str(refresh),
            'access':str(refresh.access_token),
            }
        
        return Response(data)
