from django.urls import path
from .views import SchemaCreateApiView

urlpatterns = [
    path('create-schema/', SchemaCreateApiView.as_view()),
]