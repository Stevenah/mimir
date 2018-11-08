from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('mimir.apps.dashboard.urls')),
    path('admin/', admin.site.urls),
    path('reporting/', include('mimir.apps.reporting.urls')),
    path('api/', include('mimir.apps.api.urls')),
    path('core/', include('mimir.apps.core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
