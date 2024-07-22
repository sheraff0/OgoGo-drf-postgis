from uuid import UUID
from contrib.utils.db_connection import raw_sql

from .sql import CALENDAR_FILTER


def calendar_filter(
    lat: float = None,
    lon: float = None,
    within_distance: int = None,
    not_later: float = 1,
    not_earlier: float = 4,
    category: UUID = None,
    grade: int = None,
):
    data = raw_sql(CALENDAR_FILTER(lat, lon, within_distance, not_later, not_earlier, category, grade))
    return data
