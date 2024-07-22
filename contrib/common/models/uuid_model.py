"""
Common UUID model
"""
from uuid import uuid4

from django.db import models


class UUIDModel(models.Model):
    """
    Base model to create uuid primary key
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    create_time = models.DateTimeField('Create time', auto_now_add=True, editable=False)
    update_time = models.DateTimeField('Last update time', auto_now=True, editable=False)

    class Meta:
        """
        Model is abstract
        """
        abstract = True
        ordering = ['-create_time']
