from django.contrib.auth import login, logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .utils import *
from django.shortcuts import render
from django.http import HttpResponse

def database(request):
    data = User.objects.get(pk = 1)
    username = data.username
    name = data.name
    batch = data.batch
    program = data.program
    pwd = str(data.password)
    return HttpResponse(username + " ," + name + " , " + batch + " , " + program + " , " + pwd)

class displayView(APIView):
    def post(self, request, *args, **kwargs):
        # email = request.body("email" , "")
        # email = json.loads(request.body)
        email = request.data.get("email")
        # email = emails["email"]
        # email = json.loads(request.body.decode('utf-8'))
        # print( json.loads(request.body.decode('utf-8')))
        # return Response({"message": "Got some data!"})
        return Response(get_username(email))
        # return Response("As")

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        user = IsLoggedIn(request)
        if user is not None :
            return Response(status = status.HTTP_400_BAD_REQUEST)
        email = request.data.get("email" , "")
        username = get_username(email)
        password = request.data.get("password" , "")
        try:
            user = User.objects.get(username = username)
            if user is not None:
                if CHECK_PASSWORD(password , user.password):
                    request.session["username"] = username 
                    request.session.modified = True
                    data = username + " : " + password
                    return Response(data,status = status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_401_UNAUTHORIZED)
        except :
            return Response(status = status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        if IsLoggedIn(request) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status = status.HTTP_200_OK)
    
class LogoutView(APIView):
    def post(self, request):
        if IsLoggedIn(request) is not None:
            del request.session["username"]
            return Response(status = status.HTTP_200_OK)
        return Response(status = status.HTTP_401_UNAUTHORIZED)