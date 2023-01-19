from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import register

urlpatterns = [
    path('register', register, name='create_user'),
    path('login', obtain_auth_token, name='login'),
]