"""
Project URL Configuration

"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('contrib.auth.urls')),
    path('api/v1/', include('contrib.users.urls')),
    path('api/v1/', include('apps.locations.urls')),
    path('api/v1/', include('apps.offers.urls')),
    path('api/v1/', include('apps.coupons.urls')),
    *staticfiles_urlpatterns(),
] + static(settings.MEDIA_RELATIVE_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)), *urlpatterns]

if settings.SWAGGER:

    from drf_spectacular.views import (SpectacularAPIView,
                                       SpectacularSwaggerView)

    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
        path("swagger/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs")
    ]
