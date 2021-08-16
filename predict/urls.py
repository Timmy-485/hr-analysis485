from django.urls import path
from . import views



urlpatterns = [
    # path("", views.home.as_view(), name='home'),
    path("", views.homepage, name='home'),
    path("dashboard/", views.dashboard.as_view(), name="dashboard"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]