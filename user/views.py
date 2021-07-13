from rest_framework import parsers
from .utils import (
    MAKE_PASSWORD,
    CHECK_PASSWORD,
    IsLoggedIn,
    IsRegistered,
    linkValidator,
)
from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from src.settings_email import (
    REDIRECT_LINK,
    EMAIL_BODY,
    EMAIL_HOST_USER,
    EMAIL_LINK,
    EMAIL_SUBJECT,
)
from django.shortcuts import render, redirect
from django.http import response
from django import http
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.serializers import Serializer
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from user.serializers import UserSerializer
from rest_framework.parsers import JSONParser
from placement.models import Placement
from placement.serializers import PlacementSerializer
from intern.models import Intern
from intern.serializers import InternSerializer
from django.core.mail import send_mail
import bcrypt
import regex as re
import requests


class UserPlacementsView(APIView):
    def get(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            try:
                eligible_placement_ids = list()
                all_placements = Placement.objects.all()
                for placement in all_placements:
                    if (
                        user.program in placement.eligible_programmes
                        and user.department in placement.eligible_branches
                        and user.batch in placement.eligible_batches
                    ):
                        eligible_placement_ids.append(placement.id)
                eligible_placements = Placement.objects.filter(
                    id__in=eligible_placement_ids
                )
                serializer = PlacementSerializer(eligible_placements, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserInternsView(APIView):
    def get(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            try:
                eligible_intern_ids = list()
                all_interns = Intern.objects.all()
                for intern in all_interns:
                    if (
                        user.program in intern.eligible_programmes
                        and user.department in intern.eligible_branches
                        and user.batch in intern.eligible_batches
                    ):
                        eligible_intern_ids.append(intern.id)
                eligible_interns = Intern.objects.filter(id__in=eligible_intern_ids)
                serializer = InternSerializer(eligible_interns, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserView(APIView):
    def get(self, request):
        try:
            user = IsLoggedIn(request)
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request, *args, **kwargs):
        user = IsLoggedIn(request)
        if user is not None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        try:
            user = User.objects.get(username=username, activated=True)
            if user is not None:
                if CHECK_PASSWORD(password, user.password):
                    request.session["username"] = username
                    request.session.modified = True
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)

        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        if IsLoggedIn(request) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


class Logout(APIView):
    def post(self, request):
        if IsLoggedIn(request) is not None:
            del request.session["username"]
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class Edit(APIView):
    def post(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            try:
                response1 = {"message": "Invalid URL"}
                if "github" in request.data:
                    if linkValidator(request.data["github"], "github.com"):
                        user.github = request.data["github"]
                    else:
                        return Response(response1, status=status.HTTP_400_BAD_REQUEST)
                if "linkedin" in request.data:
                    if linkValidator(request.data["linkedin"], "linkedin.com"):
                        user.linkedin = request.data["linkedin"]
                    else:
                        return Response(response1, status=status.HTTP_400_BAD_REQUEST)
                if "mastercv" in request.data:
                    if linkValidator(request.data["mastercv"], "google.com"):
                        user.mastercv = request.data["mastercv"]
                    else:
                        return Response(response1, status=status.HTTP_400_BAD_REQUEST)
                if "resume1" in request.data:
                    if linkValidator(request.data["resume1"], "google.com"):
                        user.resume1 = request.data["resume1"]
                    else:
                        return Response(response1, status=status.HTTP_400_BAD_REQUEST)
                if "resume2" in request.data:
                    if linkValidator(request.data["resume2"], "google.com"):
                        user.resume2 = request.data["resume2"]
                    else:
                        return Response(response1, status=status.HTTP_400_BAD_REQUEST)
                user.save()
                response2 = {"message": "Profile edited successfully"}
                return Response(response2, status=status.HTTP_200_OK)
            except:
                return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


def ActivationMailer(request):
    if request.method == "POST":
        try:
            roll_number = request.data["roll"]
            user_data = User.objects.get(roll=roll_number)
            sender = EMAIL_HOST_USER
            recipient = user_data.email
            name = user_data.name
            user_code = user_data.generate_verification_code()
            user_link = EMAIL_LINK["Activation"].format(code=user_code)
            subject = EMAIL_SUBJECT["Activation"]
            body = EMAIL_BODY["Activation"].format(name=name, link=user_link)
            send_mail(subject, body, sender, [recipient], fail_silently=False)
            return redirect(REDIRECT_LINK["Activation"])
        except:
            return HttpResponse("Please set up email host details!", status=206)
    else:
        return HttpResponse("Bad Request", status=400)


class RegisterationView(APIView):
    def post(self, request):
        if IsRegistered(request) is False:
            ActivationMailer(request)
            return Response(status.HTTP_202_ACCEPTED)
        if IsRegistered(request) is True:
            return Response(status.HTTP_403_FORBIDDEN)
        if IsRegistered(request) is None:
            return Response(status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)


def hashpass(password):
    password = password.encode()
    return bcrypt.hashpw(password, bcrypt.gensalt())


class SetPasswordAndActivate(APIView):
    def post(self, request, token):
        try:
            pw = request.data["password"]
            user_data = User.objects.get(verification_code=token)
            if user_data.activated == False:
                user_data.activated = True
                user_data.password = hashpass(pw).decode()
                user_data.save()
                response = {
                    "status": "success",
                    "code": status.HTTP_200_OK,
                    "message": "Password set succesfully and now you are registered",
                }
                return Response(response)
            else:
                response = {
                    "code": "status.HTTP_401_UNAUTHORIZED",
                    "message": "Token already used",
                }
                return Response(response, status=401)
        except:
            response = {
                "code": "status.HTTP_401_UNAUTHORIZED",
                "message": "Invalid token or invalid request",
            }
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class ResetPasswordEmail(APIView):
    def post(self, request):
        try:
            roll_no = request.data["roll"]
            user_data = User.objects.get(roll=roll_no)
            sender = EMAIL_HOST_USER
            recipient = user_data.email
            name = user_data.name
            user_code = user_data.generate_verification_code()
            user_link = EMAIL_LINK["PasswordReset"].format(code=user_code)
            subject = EMAIL_SUBJECT["PasswordReset"]
            body = EMAIL_BODY["PasswordReset"].format(name=name, link=user_link)
            send_mail(subject, body, sender, [recipient], fail_silently=False)
            return HttpResponse(
                "Password Reset Email sent successfully, Please Check your inbox.",
                status=200,
            )
        except:
            return HttpResponse("Please set up email host details!", status=206)


def pass_checker(old, password):
    return bcrypt.checkpw(old.encode(), password)


class ResetPassword(APIView):
    def post(self, request, token):
        try:
            new1 = request.data["new_password1"]
            new2 = request.data["new_password2"]
            old = request.data["old_password"]
            user_data = User.objects.get(verification_code=token)
            password = user_data.password
            password = password.encode()
            if user_data.activated == True:
                if new1 == new2:
                    if pass_checker(old, password) == True:
                        user_data.password = hashpass(new1).decode()
                        user_data.save()
                        response = {
                            "status": "success",
                            "code": status.HTTP_200_OK,
                            "message": "Password reset succesfull and now you can login",
                        }
                        return Response(response)
                    else:
                        response = {
                            "status": "failure",
                            "code": status.HTTP_401_UNAUTHORIZED,
                            "message": "wrong old password",
                        }
                        return Response(response)
                else:
                    response = {
                        "status": "failure",
                        "code": 401,
                        "message": "the retyped password doesn't match",
                    }
                    return Response(response)

            else:
                response = {
                    "code": "status.HTTP_401_UNAUTHORIZED",
                    "message": "Unauthorised user or Account not activated",
                }
                return Response(response, status=401)

        except:
            response = {
                "code": "status.HTTP_401_UNAUTHORIZED",
                "message": "Invalid token or invalid request",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class Populate(APIView):
    def post(self, request):
        r = requests.get("https://search.pclub.in/api/students")
        students = r.json()
        try:
            for student in students:
                cnt = student["i"]
                for key in student:
                    if student[key] == "":
                        student[key] = str(cnt)
                regex = "^[Y]"
                if re.search(regex, student["i"]):
                    batch = student["i"][:2]
                else:
                    batch = "Y" + student["i"][:2]
                try:
                    q = User.objects.get(username=student["u"])
                    q.name = student["n"]
                    q.username = student["u"]
                    q.roll = student["i"]
                    q.batch = batch
                    q.program = student["p"]
                    q.department = student["d"]
                    q.email = student["u"] + "@iitk.ac.in"
                except:
                    q = User(
                        name=student["n"],
                        username=student["u"],
                        roll=student["i"],
                        batch=batch,
                        program=student["p"],
                        department=student["d"],
                        email=student["u"] + "@iitk.ac.in",
                    )
                q.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
