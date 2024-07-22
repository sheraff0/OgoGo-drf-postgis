from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, OfferViewSet

router = DefaultRouter(trailing_slash=True)
router.register("categories", CategoryViewSet, "categories")
router.register("offers", OfferViewSet, "offers")

urlpatterns = [
    path("", include(router.urls))
]
