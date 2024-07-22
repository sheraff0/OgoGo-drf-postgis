from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.html import format_html
from django.db.models import IntegerChoices

from contrib.common.models import UUIDModel


class OfferQuerySet(models.QuerySet):
    def related(self):
        return self.prefetch_related("calendar")


class Offer(UUIDModel):
    name = models.CharField("Название", max_length=256)
    description = models.CharField("Описание", max_length=512, null=True, blank=True)
    location = models.ForeignKey("locations.Location", verbose_name="Место",
        related_name="offers", on_delete=models.CASCADE)
    grade = models.IntegerField("Уровень крутости", null=True, blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    price = models.IntegerField("Цена", null=True, blank=True)
    options = models.ManyToManyField("offers.Option", verbose_name="Опции",
        related_name="offers", blank=True)
    categories = models.ManyToManyField("offers.Category", verbose_name="Категории",
        related_name="offers", blank=True)
    fixed_time = models.BooleanField("Фиксированное время", default=False)
    reservation = models.BooleanField("Требуется резервирование мест", default=False)

    objects = OfferQuerySet.as_manager()

    def reverse_edit(self):
        return format_html("""<a href="{}" target="_blank">Редактировать</a>""".format(
            reverse("admin:offers_offer_change", args=[self.pk])
        ))
    reverse_edit.short_description = "Детали"

    def __str__(self):
        return f"{self.name} - {self.location.__str__()}"

    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"


class Calendar(UUIDModel):
    offer = models.ForeignKey("offers.Offer", verbose_name="Предложение", related_name="calendar", on_delete=models.CASCADE)
    only_dates = ArrayField(models.DateField(), verbose_name="Только эти даты", null=True, blank=True)
    except_dates = ArrayField(models.DateField(), verbose_name="Кроме этих дат", null=True, blank=True)
    only_weekdays = ArrayField(models.PositiveIntegerField(), verbose_name="Только эти дни недели", null=True, blank=True)
    except_weekdays = ArrayField(models.PositiveIntegerField(), verbose_name="Кроме этих дней недели", null=True, blank=True)
    open_time = models.TimeField("Время начала (открытия)")
    close_time = models.TimeField("Время окончания (закрытия)")

    class Meta:
        verbose_name = "Календарь"
        verbose_name_plural = "Календари"
