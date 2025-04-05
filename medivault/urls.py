from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('records/', include('records.urls')),
    path('users/', include('users.urls')),
    path('claims/', include('claims.urls')),
    path('fraud/', include('fraud_detection.urls')),
    # Add others like users, claims, etc.
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
