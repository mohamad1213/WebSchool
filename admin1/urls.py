from django.urls import path


app_name = 'administration'
from . import views
urlpatterns = [
    path('', views.index, name='admin'),
    path('profile/', views.profile, name="profile"),
    path('profile/<pk>/edit', views.accountSettings, name="profile-edit"),
    path('home/', views.beranda, name='beranda'),
    path('home/<pk>/update/', views.update_beranda, name='update_beranda'),
    path('home/<pk>/delete/', views.delete_beranda, name='delete_beranda'),
    path('tentang/', views.tentang, name='tentang'),
    path('tentang/<pk>/update/', views.update_tentang, name='update_tentang'),
    path('tentang/<pk>/delete/', views.delete_tentang, name='delete_tentang'),
    path('berita/', views.berita, name='berita'),
    path('berita/<pk>/update/', views.update_berita, name='update_berita'),
    path('berita/<pk>/delete/', views.delete_berita, name='delete_berita'),
    path('galeri/', views.galeri, name='galeri'),
    path('galeri/<pk>/update/', views.update_galeri, name='update_galeri'),
    path('galeri/<pk>/delete/', views.delete_galeri, name='delete_galeri'),
    path('prestasi/', views.prestasi, name='prestasi'),
    path('prestasi/<pk>/update/', views.update_prestasi, name='update_prestasi'),
    path('prestasi/<pk>/delete/', views.delete_prestasi, name='delete_prestasi'),
    path('ppdb/', views.ppdb, name='ppdb'),
    path('ppdb/<pk>/update/', views.update_ppdb, name='update_ppdb'),
    path('ppdb/<pk>/delete/', views.delete_ppdb, name='delete_ppdb'),

]
