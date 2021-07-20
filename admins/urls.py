from django.urls import path
from rest_framework import urlpatterns
from .views import *

urlpatterns = [
    path("interns/", InternList.as_view(), name="Internship_List"),
    path("placements/", PlacementList.as_view(), name="Placement_List"),
    path("addIntern/", AddInternship.as_view(), name="Add_Internship"),
    path("addPlacement/", AddPlacement.as_view(), name="Add_Placement"),
    path("deleteIntern/", DeleteInternship.as_view(), name="Delete_Internship"),
    path("deletePlacement/", DeletePlacement.as_view(), name="Delete_Placement"),
    path("login/", Login.as_view(), name="Login"),
    path("logout/", Logout.as_view(), name="Logout"),
    path(
        "downloadIntern/<str:key>/",
        exportInternData.as_view(),
        name="Download_Intern_Data",
    ),
    path(
        "downloadPlacement/<str:key>/",
        exportPlacementData.as_view(),
        name="Download_Placement_Data",
    ),
]
