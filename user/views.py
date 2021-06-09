from django.http.response import ResponseHeaders
from django.shortcuts import render
from rest_framework import permissions, status
from django.contrib.auth import login, logout
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import User
from .utils import *

def database(request):
    data = User.objects.get(pk = 1)
    username = data.username
    name = data.name
    batch = data.batch
    program = data.program
    return HttpResponse(username + " ," + name + " , " + batch + " , " + program)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        user = IsLoggedIn(request)
        if user is not None :
            return Response(status = status.HTTP_400_BAD_REQUEST)
        email = request.query_params.get('email' , '')
        username = get_username(email)
        # password = request.query_params.get('password' , '')
        try:
            user = User.objects.get(username = username)
            if user is not None:
                # if bcrypt.checkpw(password.encode(), user.password.encode()):
                request.session["username"] = username 
                request.session.modified = True
                return Response(status = status.HTTP_200_OK)
                # else:
                #     return Response(status = status.HTTP_401_UNAUTHORIZED)
        except :
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        