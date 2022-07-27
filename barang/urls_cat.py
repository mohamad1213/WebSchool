from django.urls import path

from . import views
urlpatterns = [
    path('', views.Category, name = 'category'),
    path('<str:pk>/delete/', views.delete_category),
    path('<str:pk>/update/', views.update_category),
]
