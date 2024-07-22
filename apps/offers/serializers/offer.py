import pytz
from django.contrib.gis.geos import Point
from rest_framework import serializers

from apps.locations.serializers import LocationSerializer
from ..models import Offer, Calendar


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = "__all__"


class OfferSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Offer
        exclude = ["create_time", "update_time"]


class OfferShortSerilizer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    fixed_time = serializers.BooleanField()


class LocationShortSerilizer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    address = serializers.CharField(required=False)
    website = serializers.CharField(required=False)
    time_zone = serializers.CharField()
    coords = serializers.ListSerializer(child=serializers.FloatField())


class OfferSearchResultsSerializer(serializers.Serializer):
    now = serializers.SerializerMethodField()
    open_time = serializers.SerializerMethodField()
    close_time = serializers.SerializerMethodField()
    wait = serializers.DurationField()
    offer = OfferShortSerilizer()
    location = LocationShortSerilizer()

    def get_now(self, obj):
        return obj["now"].astimezone(pytz.timezone(obj["location"]["time_zone"]))

    def get_open_time(self, obj):
        return obj["open_time"].astimezone(pytz.timezone(obj["location"]["time_zone"]))

    def get_close_time(self, obj):
        return obj["close_time"].astimezone(pytz.timezone(obj["location"]["time_zone"]))
