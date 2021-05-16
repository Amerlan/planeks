from django.urls import path
from .views import (
    SchemaCreateApiView,
    SchemaListApiView,
    SchemaDeleteApiView,
    SchemaGenerateApiView,
)

urlpatterns = [
    path('create-schema/', SchemaCreateApiView.as_view()),
    path('schemas/', SchemaListApiView.as_view()),
    path('delete/<str:schema_id>/', SchemaDeleteApiView.as_view()),
    path('run/', SchemaGenerateApiView.as_view()),
]
