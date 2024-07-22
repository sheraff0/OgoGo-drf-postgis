import pytz

from rest_framework import serializers

from apps.offers.serializers import OfferSerializer
from .models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField()
    offer = OfferSerializer()

    def get_start(self, obj):
        return obj.start and obj.start.astimezone(pytz.timezone(obj.offer.location.time_zone))

    class Meta:
        model = Coupon
        fields = ["id", "start", "duration", "quantity", "price", "status", "offer"]


class CouponRequireSerializer(serializers.Serializer):
    lat = serializers.FloatField(label="Широта")
    lon = serializers.FloatField(label="Долгота")
    within_distance = serializers.IntegerField(label="Радиус, м", required=False)
    not_later = serializers.IntegerField(label="Не позднее, часов")
    not_earlier = serializers.IntegerField(label="Не ранее, часов")
    category = serializers.UUIDField(label="Категория", required=False)
    grade = serializers.IntegerField(label="Уровень", required=False)
    quantity = serializers.IntegerField(label="Количество мест")
