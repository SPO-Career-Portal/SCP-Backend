from django.urls import path, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, urlpatterns
from .views import *


urlpatterns = [
    path("profile/", UserView.as_view(), name="view-user"),
    path("placements/", UserPlacementsView.as_view(), name="user_placements"),
    path("interns/", UserInternsView.as_view(), name="user_interns"),
    path("auth/login/", Login.as_view(), name="auth-login"),
    path("auth/logout/", Logout.as_view(), name="auth-logout"),
    path("edit/", Edit.as_view(), name="edit-user-profile"),
    path("register/", RegisterationView.as_view(), name="registeration"),
    path(
        "register/verify/code=<str:token>/",
        SetPasswordAndActivate.as_view(),
        name="email-activator",
    ),
    path("resetpassemail/", ResetPasswordEmail.as_view(), name="resetpass-email"),
    path("resetpass/code=<str:token>/", ResetPassword.as_view(), name="resetpass"),
]
