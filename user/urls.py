from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="auth-login"),
    path("logout/", views.LogoutView.as_view(), name="auth-logout"),
    path("database/", views.database , name="database"),
    path("display/", views.displayView.as_view() , name="display")
]
