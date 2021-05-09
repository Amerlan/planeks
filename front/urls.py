from django.urls import path
from .views import create_schema, login, schemas

urlpatterns = [
    path('create-schema/', create_schema),
    path('login/', login),
    path('schemas/', schemas),
]
