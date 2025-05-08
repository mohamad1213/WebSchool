from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='pendaftaran/password_reset_confirm.html',
        success_url='/login/'
    ), name='password_reset_confirm'),
    path('', views.index, name='home'),
    path('mi-luthful-ulum/', views.mi, name='mi'),
    path('mts-luthful-ulum/', views.mts, name='mts'),
    path('ma-luthful-ulum/', views.ma, name='ma'),
    path('berita/<pk>/', views.detail_view, name='detail'),
    path('berita/', views.list_berita, name='list-berita'),
    path('tentang-kami/', views.Tentang, name='tentang'),
    path('galeri/', views.galeri, name='list_galeri'),
    path('prestasi/', views.prestasi, name='list_prestasi'),
    path('visimisi/', views.visimisi, name='visimisi'),
    path('prestasi/<pk>/', views.detail_prestasi, name='detail_prestasi'),
    path('chat/', views.chatbot, name='chatbot'),
    path('pendaftaran/', views.daftar_santri, name='pendaftaran'),
    path('pendaftaran/berhasil/', TemplateView.as_view(template_name='pendaftaran/berhasil.html'), name='daftar_berhasil'),

    
]
