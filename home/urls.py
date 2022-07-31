from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('berita/<id>/', views.detail_view, name='detail'),
]
