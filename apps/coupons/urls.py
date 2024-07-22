from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CouponViewSet

router = DefaultRouter(trailing_slash=True)
router.register("coupons", CouponViewSet, "coupons")

urlpatterns = [
    path("", include(router.urls))
]
