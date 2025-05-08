from django.contrib import admin
from .models import *
from admin1.models import Profile

admin.site.register(Header)
admin.site.register(Home)
admin.site.register(TentangKami)
admin.site.register(Galeri)
admin.site.register(Berita)
admin.site.register(Prestasi)
admin.site.register(Pendaftaran)
admin.site.register(Profile)
admin.site.register(SantriPendaftar)
