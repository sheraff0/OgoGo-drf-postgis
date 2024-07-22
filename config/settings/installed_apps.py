"""
Installed apps settings
"""

from .env import DEBUG, SWAGGER

# developed new apps
APPS = [
    "apps.coupons",
    "apps.locations",
    "apps.offers",
    "contrib.common",
    "contrib.users"
]

THIRDPARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    *(["debug_toolbar", ] if DEBUG else []),
]

SYSTEM_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

GEO_APPS = [
    "django.contrib.gis",
]

INSTALLED_APPS = [
    *SYSTEM_APPS,
    *THIRDPARTY_APPS,
    *APPS,
    *GEO_APPS,
]

if DEBUG:
    if SWAGGER:
        INSTALLED_APPS += [
            "drf_spectacular",
        ]
else:
    INSTALLED_APPS += [
        'storages'
    ]
