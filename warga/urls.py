from django.urls import path
from .views import WargaListView,WargaDetailView,pengaduanListView,WargaCreateView,pengaduancreateView,WargaUpdateView,WargaDeleteView,pengaduanUpdateView,pengaduanDeleteView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'), # URL untuk edit
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'), # URL untuk hapus
    path('pengaduan/<int:pk>/edit/', pengaduanUpdateView.as_view(), name='pengaduan-edit'), # URL untuk edit
    path('pengaduan/<int:pk>/hapus/', pengaduanDeleteView.as_view(), name='pengaduan-hapus'), # URL untuk hapus
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'), # URL untuk form tambah
    path('pengaduan/', pengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', pengaduancreateView.as_view(), name='pengaduan-tambah'), # URL untuk form tambah
    ]