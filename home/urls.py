from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('mi-luthful-ulum/', views.mi, name='mi'),
    path('mts-luthful-ulum/', views.mts, name='mts'),
    path('ma-luthful-ulum/', views.ma, name='ma'),
    path('berita/<pk>/', views.detail_view, name='detail'),
    path('berita/', views.list_berita, name='list-berita'),
]
