from django.contrib.gis.geos import Point
from rest_framework import serializers

from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    coords = serializers.ListField(min_length=2, max_length=2,
        child=serializers.FloatField(), required=False)
    #distance = serializers.SerializerMethodField()

    def get_distance(self, instance):
        return instance.distance and instance.distance.m

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if (coords := ret.pop("coords", None)) is not None:
            ret["coords"] = coords[::-1]
        return ret

    def validate_coords(self, value):
        if value:
            return Point(*value[::-1], srid=4326)

    class Meta:
        model = Location
        exclude = ["create_time", "update_time"]
