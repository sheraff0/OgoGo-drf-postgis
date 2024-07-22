from django.contrib import admin
from django.forms import ModelForm

from apps.offers.models import Offer
from .models import Location
from .widgets import PointInputWidget


class OfferInline(admin.StackedInline):
    model = Offer
    extra = 0
    readonly_fields = ["reverse_edit"]


class LocationForm(ModelForm):
    class Meta:
        model = Location
        widgets = {
            "coords": PointInputWidget
        }
        fields = "__all__"


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    inlines = [OfferInline]
    search_fields = ["name"]
    ordering = ["-create_time"]