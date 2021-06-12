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
from placement.models import Placement
from placement.serializers import PlacementSerializer
from intern.models import Intern
from intern.serializers import InternSerializer


class UserPlacementsView(APIView):
    def get(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            try:
                eligible_placement_ids = list()
                all_placements = Placement.objects.all()
                for placement in all_placements:
                    if user.program in placement.eligible_programmes and user.department in placement.eligible_branches and user.batch in placement.eligible_batches:
                        eligible_placement_ids.append(placement.id)
                eligible_placements = Placement.objects.filter(id__in=eligible_placement_ids)
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
                    if user.program in intern.eligible_programmes and user.department in intern.eligible_branches and user.batch in intern.eligible_batches:
                        eligible_intern_ids.append(intern.id)
                eligible_interns = Intern.objects.filter(id__in=eligible_intern_ids)
                serializer = InternSerializer(eligible_interns, many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
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
