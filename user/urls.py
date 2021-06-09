from django.urls import path, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, urlpatterns

from .import views 

app_name='User'

urlpatterns =[
    path('users/',views.Userview.as_view(),name="view-user")
]