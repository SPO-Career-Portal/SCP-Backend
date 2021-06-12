from django.http import response
from django.shortcuts import render
from django import http
from django.http.response import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.serializers import Serializer
from user.serializers import UserSerializer
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from .utils import *
from rest_framework.parsers import JSONParser


class Userview(APIView):
    def get(self, request):
        try:
            user = IsLoggedIn(request)
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
