from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
# Create your views here.


class LoginApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request: Request):
        data = request.data
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutApiView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
