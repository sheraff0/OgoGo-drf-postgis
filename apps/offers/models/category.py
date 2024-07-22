from django.db import models

from contrib.common.models import UUIDModel


class Category(UUIDModel):
    name = models.CharField(max_length=256)
    description = models.CharField("Описание", max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
