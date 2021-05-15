from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .models import Schema, Column
from .serializers import SchemaSerializer
from .services import create_columns


# Create your views here.


class SchemaCreateApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        schema_data = request.data
        fields_data = schema_data.pop('data')
        Schema.objects.all().delete()
        Column.objects.all().delete()
        schema_serializer = SchemaSerializer(data=schema_data)
        schema_serializer.is_valid(raise_exception=True)
        schema = schema_serializer.save()
        create_columns(data_list=fields_data, schema=schema)

        return Response(status=status.HTTP_201_CREATED)


class SchemaListApiView(APIView):
    pass