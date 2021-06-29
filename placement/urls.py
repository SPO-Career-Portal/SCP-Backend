from django.urls import path, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, urlpatterns
from .views import *


urlpatterns = [
    path("register/", Register.as_view(), name="register-user"),
]
