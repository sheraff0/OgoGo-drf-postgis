from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LocationViewSet

router = DefaultRouter(trailing_slash=True)
router.register("locations", LocationViewSet, "locations")

urlpatterns = [
    path("", include(router.urls))
]
