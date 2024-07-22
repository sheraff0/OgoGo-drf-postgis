from django.core.exceptions import ValidationError
from zoneinfo import ZoneInfo


def validate_timezone(value):
    try:
        assert ZoneInfo(value)
    except:
        raise ValidationError("Invalid timezone!")
