from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import *
from placement.models import Placement
from placement.serializers import PlacementSerializer


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
                eligible_placements = Placement.objects.filter(
                    id__in=eligible_placement_ids
                )
                serializer = PlacementSerializer(eligible_placements, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# Create your views here.
