from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf
from rest_framework.decorators import api_view
from .models import Admin
from rest_framework.views import APIView
from .utils import IsLoggedIn
from intern.models import Intern
from placement.models import Placement
from user.models import User, InternResume, PlacementResume
from .serializers import InternSerializer, PlacementSerializer
from rest_framework.response import Response
from rest_framework import status
from user.utils import CHECK_PASSWORD
import csv


class Login(APIView):
    def post(self, request, *args, **kwargs):
        user = IsLoggedIn(request)
        if user is not None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        try:
            user = Admin.objects.get(username=username)
            if user is not None:
                if CHECK_PASSWORD(password, user.password):
                    request.session["username"] = username
                    request.session.modified = True
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    def post(self, request):
        if IsLoggedIn(request) is not None:
            del request.session["username"]
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class InternList(APIView):
    def get(self, request):
        if IsLoggedIn(request) is not None:
            try:
                internships = Intern.objects.all()
                serializer = InternSerializer(internships, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class PlacementList(APIView):
    def get(self, request):
        if IsLoggedIn(request) is not None:
            try:
                placements = Placement.objects.all()
                serializer = PlacementSerializer(placements, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class AddInternship(APIView):
    def post(self, request):
        if IsLoggedIn(request) is not None:
            try:
                intern = Intern(
                    intern_name=request.data["intern_name"],
                    company=request.data["company"],
                    role=request.data["role"],
                    description=request.data["description"],
                    eligible_batches=request.data["eligible_batches"],
                    eligible_branches=request.data["eligible_branches"],
                    eligible_programmes=request.data["eligible_programmes"],
                    deadline=request.data["deadline"],
                )
                intern.save()
                return Response(status=status.HTTP_200_OK)
            except:
                response = {"message": "Invalid Information"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class AddPlacement(APIView):
    def post(self, request):
        if IsLoggedIn(request) is not None:
            try:
                placement = Placement(
                    placement_name=request.data["placement_name"],
                    company=request.data["company"],
                    role=request.data["role"],
                    description=request.data["description"],
                    eligible_batches=request.data["eligible_batches"],
                    eligible_branches=request.data["eligible_branches"],
                    eligible_programmes=request.data["eligible_programmes"],
                    deadline=request.data["deadline"],
                )
                placement.save()
                return Response(status=status.HTTP_200_OK)
            except:
                response = {"message": "Invalid Information"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class DeleteInternship(APIView):
    def delete(self, request):
        if IsLoggedIn(request) is not None:
            try:
                key = request.data["key"]
                intern = Intern.objects.get(key=key)
                intern.delete()
                return Response(status=status.HTTP_200_OK)
            except:
                response = {"message": "Invalid key"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class DeletePlacement(APIView):
    def delete(self, request):
        if IsLoggedIn(request) is not None:
            try:
                key = request.data["key"]
                placement = Placement.objects.get(key=key)
                placement.delete()
                return Response(status=status.HTTP_200_OK)
            except:
                response = {"message": "Invalid key"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class exportInternData(APIView):
    def get(self, request, key):
        if IsLoggedIn(request) is not None:
            try:
                response = HttpResponse(content_type="text/csv")
                intern = Intern.objects.get(key=key)
                response["Content-Disposition"] = (
                    "attachment; filename=" + intern.intern_name + ".csv"
                )

                writer = csv.writer(response)
                writer.writerow(
                    [
                        "Name",
                        "Username",
                        "Roll",
                        "Batch",
                        "Program",
                        "Department",
                        "Github",
                        "Linkedin",
                        "MasterCV",
                        "Resume",
                    ]
                )

                users = User.objects.filter(interns_applied_for=intern)
                for user in users:
                    intern_resume = InternResume.objects.filter(
                        user=user, intern=intern
                    )
                    writer.writerow(
                        [
                            user.name,
                            user.username,
                            user.roll,
                            user.batch,
                            user.program,
                            user.department,
                            user.github,
                            user.linkedin,
                            user.mastercv,
                            intern_resume[0].resume,
                        ]
                    )
                response.status_code = status.HTTP_200_OK
                return response
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class exportPlacementData(APIView):
    def get(self, request, key):
        if IsLoggedIn(request) is not None:
            try:
                response = HttpResponse(content_type="text/csv")
                placement = Placement.objects.get(key=key)
                response["Content-Disposition"] = (
                    "attachment; filename=" + placement.placement_name + ".csv"
                )

                writer = csv.writer(response)
                writer.writerow(
                    [
                        "Name",
                        "Username",
                        "Roll",
                        "Batch",
                        "Program",
                        "Department",
                        "Github",
                        "Linkedin",
                        "MasterCV",
                        "Resume",
                    ]
                )

                users = User.objects.filter(placements_applied_for=placement)
                for user in users:
                    placement_resume = PlacementResume.objects.filter(
                        user=user, placement=placement
                    )
                    writer.writerow(
                        [
                            user.name,
                            user.username,
                            user.roll,
                            user.batch,
                            user.program,
                            user.department,
                            user.github,
                            user.linkedin,
                            user.mastercv,
                            placement_resume[0].resume,
                        ]
                    )
                response.status_code = status.HTTP_200_OK
                return response
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# Create your views here.
