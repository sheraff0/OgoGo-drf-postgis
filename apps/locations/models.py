from django.db.models import F, Value
from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.utils.translation import gettext_lazy as _

from contrib.common.models import UUIDModel
from contrib.utils.date_time import validate_timezone


class LocationQuerySet(models.QuerySet):
    def distance(self, point=[44.893844, 37.616726]):
        return self.annotate(
            distance=Distance(F("coords"), Value(Point(point[::1], srid=4326)))
        )


class Location(UUIDModel):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    website = models.CharField(max_length=256)
    coords = models.PointField(geography=True)
    time_zone = models.CharField("Часовой пояс", max_length=32,
        default="Europe/Moscow", validators=[validate_timezone])

    objects = LocationQuerySet.as_manager()

    def __str__(self):
        return f"{self.name} ({self.address or '?'} - {self.time_zone})"

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
