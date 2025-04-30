from django.urls import path
from admin1.views import ProfileView

app_name = 'administration'
from . import views
urlpatterns = [
    # path('profile/', ProfileView.as_view(), name='profile'),
    path('', views.index, name='admin'),
    path("chatbot/", views.chatbot_view, name="chatbot_api"),
    path('generate-keywords/', views.generate_keywords, name='generate_keywords'),
    path('generate-article/', views.generate_article, name='generate_article'),
    path('edit-artikel/<int:pk>/', views.edit_artikel, name='article_editor'),
    path('preview/<int:pk>/', views.preview_article, name='preview_article'),
    path('save/<int:pk>/', views.save_article, name='save_article'),
    path('list/', views.article_list, name='article_list'),
    path('box', views.box, name='box'),
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
    path('prestasi/create/', views.prestasiCreate, name='create_prestasi'),
    path('prestasi/<pk>/update/', views.update_prestasi, name='update_prestasi'),
    path('prestasi/<pk>/delete/', views.delete_prestasi, name='delete_prestasi'),
    path('ppdb/', views.ppdb, name='ppdb'),
    path('ppdb/<pk>/update/', views.update_ppdb, name='update_ppdb'),
    path('ppdb/<pk>/delete/', views.delete_ppdb, name='delete_ppdb'),
    path('tentang-kami/', views.tentang_list, name='tentang_list'),
    path('tentang-kami/create/', views.TentangKamiCreate, name='Create_tentang'),
    path('visimisi/', views.visimisi_list, name='visimisi_list'),
    path('visimisi/create/', views.visimisiCreate, name='create_visimisi'),
    
    

]
