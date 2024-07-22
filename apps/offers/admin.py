from django.contrib import admin

from .models import Category, Option, Offer, Calendar

admin.site.register(Category)
admin.site.register(Option)


class CalendarInline(admin.StackedInline):
    model = Calendar
    extra = 0
    ordering = ["-create_time"]


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    inlines = [CalendarInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("location")
