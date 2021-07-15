from user.utils import IsLoggedIn
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from django.http import response
from django import http
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from placement.models import Placement


# Create your views here.


class Register(APIView):
    def post(self, request):

        user = IsLoggedIn(request)
        if user is not None:
            try:
                placement_applied = Placement.objects.get(key=request.data["token"])
                if (
                    user.program in placement_applied.eligible_programmes
                    and user.department in placement_applied.eligible_branches
                    and user.batch in placement_applied.eligible_batches
                ):
                    user.placements_applied_for.add(placement_applied)
                    response = {
                        "message": "You have successfully registered for this placement offer"
                    }
                    return Response(response, status=status.HTTP_200_OK)
                else:
                    response = {
                        "message": "You are not eligible for this placement offer"
                    }
                    return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)



class CreatePlacementView(APIView):
    
    def post(self, request):
        try:
            user = IsLoggedIn(request)
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            placement_name = request.data.get("placement_name", "")
            company=request.data.get("company", "")
            deadline=request.data.get("deadline", "")
            role=request.data.get("role", "")
            description=request.data.get("decription", "")
           
            Placement.objects.create(placement_name=placement_name, company=company, duration=deadline,role=role,description=description)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)