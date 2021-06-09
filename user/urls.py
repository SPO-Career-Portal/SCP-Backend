from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="auth-login"),
    path("logout/", views.Logout.as_view(), name="auth-logout"),
]
