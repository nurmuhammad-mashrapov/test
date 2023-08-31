
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/advertisement/", include("apps.advertisement.urls")),
    path("api/v1/promt/", include("apps.promt.urls")),
    path("api/v1/education/", include("apps.education.urls")),
    path("api/v1/neauralnetwork/", include("apps.neauralnetwork.urls")),
    path("api/v1/midjouney/", include("apps.midjouney.urls")),

]
urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
