# warga/api_views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
# 1. IMPOR FILTER BACKEND
from rest_framework.filters import SearchFilter, OrderingFilter 
from .models import Pengaduan, Warga
from .serializers import PengaduanSerializer, WargaSerializer

# ViewSet Warga
class WargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk Warga.
    Fitur: Pagination (Otomatis), Searching, Ordering.
    """
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # 2. KONFIGURASI FILTER (PERTEMUAN 10)
    filter_backends = [SearchFilter, OrderingFilter]
    
    # Kolom mana saja yang bisa dicari (keyword search)
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    
    # Kolom mana saja yang bisa diurutkan (sorting)
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']


# ViewSet Pengaduan (CHALLENGE SELESAI)
class PengaduanViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk Pengaduan.
    Fitur: Pagination (Otomatis), Searching, Ordering.
    """
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor') # Default urut dari yang terbaru
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser]

    # 3. IMPLEMENTASI CHALLENGE PADA PENGADUAN
    filter_backends = [SearchFilter, OrderingFilter]
    
    # Bisa cari berdasarkan judul atau isi deskripsi
    search_fields = ['judul', 'deskripsi']
    
    # Bisa urutkan berdasarkan status atau tanggal lapor
    ordering_fields = ['status', 'tanggal_lapor']