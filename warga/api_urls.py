from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Impor ViewSet baru yang kita buat di api_views.py
from .api_views import WargaViewSet, PengaduanViewSet 

# 1. Buat sebuah router
router = DefaultRouter()

# 2. Daftarkan ViewSet Warga (Praktikum)
# Ini akan membuat URL:
#   /api/warga/ -> (GET untuk list, POST untuk create)
#   /api/warga/<pk>/ -> (GET untuk detail, PUT/PATCH untuk update, DELETE untuk hapus)
router.register(r'warga', WargaViewSet, basename='warga')

# 3. Daftarkan ViewSet Pengaduan (Challenge)
# Ini akan membuat URL:
#   /api/pengaduan/ -> (GET untuk list, POST untuk create)
#   /api/pengaduan/<pk>/ -> (GET untuk detail, PUT/PATCH untuk update, DELETE untuk hapus)
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')

# 4. URL API sekarang ditentukan secara otomatis oleh router.
# File data_kelurahan/urls.py Anda sudah benar mengarahkan /api/ ke file ini,
# jadi tidak perlu ada perubahan di sana.
urlpatterns = [
    path('', include(router.urls)),
]