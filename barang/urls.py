from django.urls import path

from . import views
urlpatterns = [
    # path('', views.login, name='login'),
    path('', views.barang, name = 'barang'),
    path('create_barang', views.create_barang, name = 'create_barang'),
    path('<str:pk>/detail/', views.detail_barang),
    path('<str:pk>/delete/', views.delete_barang),
    path('<str:pk>/update/', views.update_barang),
]
