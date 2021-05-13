from django.urls import path
from .views import CreateSchemaApiView

urlpatterns = [
    path('create-schema/', CreateSchemaApiView.as_view()),
]