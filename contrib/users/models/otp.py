import time

from django.conf import settings
from django.db import models, transaction


class OTP(models.Model):
    email = models.EmailField('email', unique=True, null=True)
    phone = models.CharField(unique=True, max_length=70, blank=True, null=True)
    code = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    attempts = models.IntegerField(default=3)
    last_update = models.DateTimeField()

    @property
    def expired(self):
        return (delta := int(
            self.last_update.timestamp() + settings.OTP_EXPIRATION - time.time()
        )) < 0

    @transaction.atomic
    def verify(self, code):
        assert self.attempts > 0
        if self.code == code:
            self.is_verified = True
        else:
            self.attempts -= 1
        self.save()
        return self.is_verified
