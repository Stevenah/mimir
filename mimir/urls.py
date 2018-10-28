from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reporting/', include('mimir.apps.reporting.urls')),
    path('api/', include('mimir.apps.api.urls')),
    path('core/', include('mimir.apps.core.urls')),
]
