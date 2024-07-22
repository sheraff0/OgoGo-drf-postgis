from django.db import models
from django.utils.translation import gettext_lazy as _

from contrib.common.models import UUIDModel


class Option(UUIDModel):
    name = models.CharField("Название", max_length=256)
    description = models.CharField("Описание", max_length=256, null=True, blank=True)
    desirable = models.BooleanField("Желательно", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Опция"
        verbose_name_plural = "Опции"
