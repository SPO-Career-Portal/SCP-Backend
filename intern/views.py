from user.utils import IsLoggedIn
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from django.http import response
from django import http
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from intern.models import Intern


# Create your views here.

class Register(APIView):
    def post(self, request):
        # if request.method == "POST":
        user = IsLoggedIn(request)
        if user is not None:
            try:
                intern_applied = Intern.objects.get(key=request.data['token'])
                if (
                    user.program in intern_applied.eligible_programmes
                    and user.department in intern_applied.eligible_branches
                    and user.batch in intern_applied.eligible_batches
                ):
                    user.interns_applied_for.add(intern_applied)
                    response = {
                        "message": "You have successfully registered for this internship"
                    }
                    return Response(response, status=status.HTTP_200_OK)
                else:
                    response = {
                        "message": "You are not eligible for this intership"}
                    return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
