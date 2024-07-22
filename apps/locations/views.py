from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin

from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(UpdateModelMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.distance().all()
    http_method_names = ["get", "post", "patch", "delete"]
