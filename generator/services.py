from .serializers import ColumnSerializer
from typing import List

def create_columns(*, data: List):
    for col in data:
        serializer = ColumnSerializer(data=col)
        serializer.is_valid(raise_exception=True)
