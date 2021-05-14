from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import SchemaSerializer, ColumnSerializer


# Create your views here.


class SchemaCreateApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        schema_data = request.data
        field_data = schema_data.pop('data')
        schema_serializer = SchemaSerializer(data=schema_data)
        schema_serializer.is_valid(raise_exception=True)
        print(schema_serializer.data)

        return Response(status=status.HTTP_201_CREATED)
