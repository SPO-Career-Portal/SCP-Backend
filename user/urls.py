from .views import *
from django.urls import path

urlpatterns = [
    path(
        "placements/",
        UserPlacementsView.as_view(),
        name="user_placements",
    )
]
