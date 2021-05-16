from .models import Schema, Column
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
            'id', 'name', 'pretty_update_at',
        )