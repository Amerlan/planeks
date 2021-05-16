from .models import Schema, Column, Dataset
from rest_framework import serializers


class SchemaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = (
            'id', 'name', 'separator', 'string_character'
        )


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = (
            'name', 'schema', 'field_type',
            'lower_bound', 'upper_bound', 'sentence_count'
        )


class SchemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = (
            'id', 'name', 'pretty_updated_at',
        )


class DatasetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = (
            'schema', 'status', 'download_url'
        )


class DatasetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = (
            'id', 'pretty_created_at', 'status', 'download_url'
        )


class SchemaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = (
            'id', 'name', 'separator', 'string_character',
        )
