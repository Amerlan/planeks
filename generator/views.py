from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class CreateSchemaApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        print(data)
        return Response(status=status.HTTP_201_CREATED)
