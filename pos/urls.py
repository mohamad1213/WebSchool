from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader import views as ckeditor_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('administration/', include('admin1.urls')),
    # path('barang/', include('barang.urls')),
    # path('category/', include('barang.urls_cat')),
    # path('transaksi/', include('transaksi.urls')),
    path('accounts/', include('account.urls')),
    path('ckeditor/upload/', ckeditor_views.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', ckeditor_views.browse, name='ckeditor_browse'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)