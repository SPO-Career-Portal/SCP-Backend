from user.utils import IsLoggedIn
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import PlacementResume
from rest_framework import status
from placement.models import Placement
from django.utils import timezone


# Create your views here.


class Register(APIView):
    def post(self, request):

        user = IsLoggedIn(request)
        if user is not None:
            try:
                placement_applied = Placement.objects.get(key=request.data["key"])
                if placement_applied.deadline < timezone.now():
                    response = {
                        "message": "No more submissions are being accepted for this offer"
                    }
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
                if request.data["resume"].lower() == "resume1":
                    resume = user.resume1
                elif request.data["resume"].lower() == "resume2":
                    resume = user.resume2
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                if (
                    user.program in placement_applied.eligible_programmes
                    and user.department in placement_applied.eligible_branches
                    and user.batch in placement_applied.eligible_batches
                ):
                    if user.github and user.linkedin and user.mastercv:
                        if resume:
                            if PlacementResume.objects.filter(
                                user=user, placement=placement_applied
                            ).exists():
                                response = {
                                    "message": "You have already applied for this offer"
                                }
                                return Response(
                                    response, status=status.HTTP_400_BAD_REQUEST
                                )
                            else:
                                resume_relation = PlacementResume(
                                    user=user,
                                    placement=placement_applied,
                                    resume=resume,
                                )
                            resume_relation.save()
                            response = {
                                "message": "You have successfully registered for this placement offer"
                            }
                            return Response(response, status=status.HTTP_200_OK)
                    response = {"message": "User profile update incomplete"}
                    return Response(response, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    response = {
                        "message": "You are not eligible for this placement offer"
                    }
                    return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
