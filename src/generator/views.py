from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Schema
from .serializers import SchemaCreateSerializer, SchemaListSerializer
from .services import create_columns
from .tasks import generate_csv


class SchemaCreateApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        schema_data = request.data
        fields_data = schema_data.pop('data')
        schema_serializer = SchemaCreateSerializer(data=schema_data)
        schema_serializer.is_valid(raise_exception=True)
        schema = schema_serializer.save()
        create_columns(data_list=fields_data, schema=schema)

        return Response(status=status.HTTP_201_CREATED)


class SchemaListApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        queryset = Schema.objects.all()
        serializer = SchemaListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class SchemaDeleteApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, schema_id):
        Schema.objects.get(id=schema_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SchemaGenerateApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.data
        schema = Schema.objects.last()
        # schema = get_object_or_404(Schema, id=data['schema_id'])
        generate_csv(qty=int(data['qty']), schema=schema)
        return Response(status=status.HTTP_201_CREATED)
