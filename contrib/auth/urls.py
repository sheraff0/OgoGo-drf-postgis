from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LoginView, RegisterView, OTPViewSet

otp_router = DefaultRouter()
otp_router.register("", OTPViewSet, "otp")

urlpatterns = [
    #path("login/", LoginView.as_view(), name="login"),
    #path("register/", RegisterView.as_view(), name="register"),
    path("otp/", include(otp_router.urls)),
]
