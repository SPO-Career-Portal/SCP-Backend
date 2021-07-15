from user.utils import IsLoggedIn
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from intern.models import Intern
from user.models import InternResume

# Create your views here.


class Register(APIView):
    def post(self, request):

        user = IsLoggedIn(request)
        if user is not None:
            try:
                intern_applied = Intern.objects.get(key=request.data["key"])
                if request.data["resume"].lower() == "resume1":
                    resume = user.resume1
                elif request.data["resume"].lower() == "resume2":
                    resume = user.resume2
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                if (
                    user.program in intern_applied.eligible_programmes
                    and user.department in intern_applied.eligible_branches
                    and user.batch in intern_applied.eligible_batches
                ):
                    if user.github and user.linkedin and user.mastercv:
                        if resume:
                            if InternResume.objects.filter(
                                user=user, intern=intern_applied
                            ).exists():
                                resume_relation = InternResume.objects.get(
                                    user=user, intern=intern_applied
                                )
                                resume_relation.resume = resume
                            else:
                                resume_relation = InternResume(
                                    user=user, intern=intern_applied, resume=resume
                                )
                            resume_relation.save()
                            response = {
                                "message": "You have successfully registered for this internship"
                            }
                            return Response(response, status=status.HTTP_200_OK)
                    response = {"message": "User profile update incomplete"}
                    return Response(response, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    response = {"message": "You are not eligible for this internship"}
                    return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
