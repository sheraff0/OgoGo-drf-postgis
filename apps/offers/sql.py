from uuid import UUID

EXTRACT_POINTS = lambda geo_data: f"""
    (ST_AsGeoJSON(
        ST_FlipCoordinates(
            {geo_data}
        )
    )::jsonb->>'coordinates')::json
"""


def CALENDAR_FILTER(
    lat: float = None,
    lon: float = None,
    within_distance: int = None,
    not_later: float = 1,
    not_earlier: float = 4,
    category: UUID = None,
    grade: int = None,
):
    location = [lat, lon]
    at_tz = "AT TIME ZONE time_zone"

    def dt_with_delta(
        field: str,
        tz_local: bool = False
    ):
        if "close_time" in field:
            interday = " + CASE WHEN close_time < open_time THEN INTERVAL '24 hours' ELSE INTERVAL '0 hours' END"
            field += interday
        return f"(current_date + delta::interval + {field}) {at_tz}"

    # Time filter
    time_filter = f"""CASE
    WHEN oo.fixed_time THEN now() BETWEEN
            ({dt_with_delta(f"open_time - INTERVAL '{not_earlier} hours'")})
        AND
            ({dt_with_delta(f"open_time - INTERVAL '{not_later} hours'")})
    ELSE now() BETWEEN
            ({dt_with_delta(f"open_time - INTERVAL '{not_earlier} hours'")})
        AND
            ({dt_with_delta(f"close_time - INTERVAL '{not_later} hours'")})
    END
"""

    # Geospatial distance filter
    distance_filter = f"""
AND ST_DWithin(
    ll.coords,
    'SRID=4326;POINT({" ".join(map(str, location[::-1]))})'::geography,
    {within_distance}
)""" if location and within_distance else ""

    # Week days filter
    dow = "EXTRACT(ISODOW FROM (now() + delta::interval) AT TIME ZONE time_zone)::int"
    dow_filter = f"""
AND (oc.except_weekdays IS NULL OR NOT ARRAY[{dow}] <@ oc.except_weekdays)
AND (array_length(oc.only_weekdays, 1) IS NULL OR ARRAY[{dow}] <@ oc.only_weekdays)
"""

    # Dates filter
    today = "((now() + delta::interval) AT TIME ZONE time_zone)::date"
    dates_filter = f"""
AND (oc.except_dates IS NULL OR NOT ARRAY[{today}] <@ oc.except_dates)
AND (array_length(oc.only_dates, 1) IS NULL OR ARRAY[{today}] <@ oc.only_dates)
"""

    #Category filter
    category_join_filter = f"""
JOIN (
    SELECT offer_id, COUNT(*)
    FROM offers_offer_categories
    WHERE category_id='{str(category)}'
    GROUP BY offer_id
) ooc ON ooc.offer_id=oo.id
""" if category else ""

    # Grade filter
    grade_filter = f"""
AND oo.grade={grade}
""" if grade else ""

    return f"""
SELECT now() now,
    ({dt_with_delta("open_time")}) open_time,
    ({dt_with_delta(f"close_time")}) close_time,
    GREATEST('0 hours'::interval, ({dt_with_delta("open_time")}) - now()) wait,
    {dow} dow,
    json_build_object(
        'id', oo.id,
        'name', oo.name,
        'description', oo.description,
        'price', COALESCE (oo.price, 0),
        'fixed_time', oo.fixed_time
    ) offer,
    json_build_object(
        'id', ll.id,
        'name', ll.name,
        'address', ll.address,
        'website', ll.website,
        'time_zone', ll.time_zone,
        'coords', {EXTRACT_POINTS("ll.coords::geometry")}
    ) location
FROM offers_calendar oc
JOIN offers_offer oo ON oo.id=oc.offer_id
JOIN locations_location ll ON ll.id=oo.location_id
{category_join_filter},
(VALUES ('-1 days'), ('0 days'), ('1 days')) interval(delta)
WHERE {time_filter}
{distance_filter}
{dow_filter}
{dates_filter}
{grade_filter}
ORDER BY wait
;
"""
