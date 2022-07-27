from django.urls import path

from . import views
urlpatterns = [
    path('', views.customer, name = 'customer'),
    path('create_customer', views.create_customer, name = 'create_customer'),
    path('<str:id>/detail/', views.detail_customer),
    path('<id>/delete/', views.delete_customer),
    path('<id>/update/', views.update_customer),
]
