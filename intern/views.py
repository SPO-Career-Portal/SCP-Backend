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
                intern_applied = Intern.objects.get(key=request.data["token"])
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
                    response = {"message": "You are not eligible for this intership"}
                    return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class CreateInternView(APIView):
    
    def post(self, request):
        try:
            user = IsLoggedIn(request)
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            intern_name = request.data.get("intern_name", "")
            company=request.data.get("company", "")
            deadline=request.data.get("deadline", "")
            role=request.data.get("role", "")
            description=request.data.get("decription", "")
           
            Intern.objects.create(intern_name=intern_name, company=company, duration=deadline,role=role,description=description)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# class DeletePostView(APIView):

#     def delete(self, request):
#         user = IsLoggedIn(request)
#         if user is not None:
#             try:
#                 pk = request.data.get("pk", "")
#                 intern = Intern.objects.get(pk=pk)
#                 if intern is not None:
#                     key = intern.key
#                     if key == user :
#                         intern.delete()
#                         return Response(status=status.HTTP_204_NO_CONTENT)
#                     else:
#                         return Response(status=status.HTTP_401_UNAUTHORIZED)
#                 else:
#                     return Response(status = status.HTTP_400_BAD_REQUEST)
#             except:
#                 return Response(status = status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)