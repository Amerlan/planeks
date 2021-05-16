from django.urls import path
from .views import LoginApiView, LogoutApiView

urlpatterns = [
    path('logout/', LogoutApiView.as_view()),
    path('login/', LoginApiView.as_view()),
]
