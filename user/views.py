from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import *
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
                    if user.program in placement.eligible_programmes:
                        if user.department in placement.eligible_branches:
                            if user.batch in placement.eligible_batches:
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
                    if user.program in intern.eligible_programmes:
                        if user.department in intern.eligible_branches:
                            if user.batch in intern.eligible_batches:
                                eligible_intern_ids.append(intern.id)
                eligible_interns = Intern.objects.filter(id__in=eligible_intern_ids)
                serializer = InternSerializer(eligible_interns, many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# Create your views here.
