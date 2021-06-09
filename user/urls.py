from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="auth-login"),
    path("database/", views.database , name="login")
]
