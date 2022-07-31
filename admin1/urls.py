from django.urls import path


app_name = 'administration'
from . import views
urlpatterns = [
    path('', views.index, name='admin'),
    path('home/', views.beranda, name='beranda'),
    path('tentang/', views.tentang, name='tentang'),
    path('berita/', views.berita, name='berita'),
    path('galeri/', views.galeri, name='galeri'),
    path('ppdb/', views.ppdb, name='ppdb'),
]
