from django.urls import path
from . import views

urlpatterns = [
    path("auth/login/", views.Login.as_view(), name="auth-login"),
    path("auth/logout/", views.Logout.as_view(), name="auth-logout"),
]
