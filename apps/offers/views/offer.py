from uuid import UUID
from random import choice

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from ..models import Offer
from ..serializers import OfferSerializer, OfferSearchResultsSerializer
from ..querysets import calendar_filter


class OfferViewSet(GenericViewSet):
    http_method_names = ["get", "post"]

    @extend_schema(
        parameters=[
            OpenApiParameter('lat', description="Широта", required=True, type=float),
            OpenApiParameter('lon', description="Долгота", required=True, type=float),
            OpenApiParameter('within_distance', description="Радиус, м", required=False, type=int, default=2000),
            OpenApiParameter('not_later', description="Не позднее, часов", required=True, type=float, default=1),
            OpenApiParameter('not_earlier', description="Не ранее, часов", required=True, type=float, default=4),
            OpenApiParameter('category', description="Категория", required=False, type=UUID),
            OpenApiParameter('grade', description="Уровень", required=False, type=int),
        ],
        responses=OfferSearchResultsSerializer,
    )
    @action(detail=False)
    def search(self, request, location=None):
        lat, lon, within_distance, not_later, not_earlier, category, grade = map(request.GET.get, (
            "lat", "lon", "within_distance", "not_later", "not_earlier", "category", "grade"))
        if data := calendar_filter(lat, lon, within_distance, not_later, not_earlier, category, grade):
            closest = data[0]["wait"]
            obj = choice([x for x in data if x["wait"] == closest])
            serializer = OfferSearchResultsSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"errors": {"details": ["Not found"]}}, status=status.HTTP_404_NOT_FOUND)
