from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('warga.urls')),  # arahkan ke aplikasi warga
    path('api/', include('warga.api_urls')),
]
