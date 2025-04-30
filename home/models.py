from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.utils.text import slugify
class Header(models.Model):
    id_header = models.AutoField(primary_key=True)
    logo = models.FileField( upload_to='media/images/',blank=True, null=True)
    navbar1 = models.CharField(max_length=100)
    navbar2 = models.CharField(max_length=100)
    navbar3 = models.CharField(max_length=100)
    navbar4 = models.CharField(max_length=100)
    navbar5 = models.CharField(max_length=100)
    navbar6 = models.CharField(max_length=100)
    dropdown1 = models.CharField(max_length=100)
    dropdown2 = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Home(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='home')
    id_home = models.AutoField(primary_key=True)
    logo = models.FileField( upload_to='media/images/',blank=True, null=True)
    h1 = models.CharField(max_length=100)
    nama_pondok = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    telpon = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class TentangKami(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='tentang')
    id_tentangkami = models.AutoField(primary_key=True)
    image = models.FileField( upload_to='media/images/',blank=True, null=True)
    desc = models.TextField()
    nama_pengasuh = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
class Galeri(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='galeri')
    id_galeri = models.AutoField(primary_key=True)
    image = models.FileField( upload_to='media/images/galeri/',blank=True, null=True)
    desc = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Berita(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='berita')
    id_berita = models.AutoField(primary_key=True)
    nama_penulis = models.CharField(max_length=100)
    judul = models.CharField(default= '',max_length=100)
    isi = models.TextField(default= '')
    penerbit = models.CharField(max_length=100,blank=True, null=True)
    image = models.FileField(upload_to='media/images/berita/',blank=True, null=True)
    desc = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
class Prestasi(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='prestasi')
    nama = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    lokasi = models.CharField(max_length=255)
    content = RichTextUploadingField()
    image = models.FileField(upload_to='media/images/prestasi/',blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.nama

class Pendaftaran(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='daftar')
    id_daftar = models.AutoField(primary_key=True)
    link_daftar = models.CharField(max_length=100)
    brosur = models.FileField( upload_to='media/images/daftar/',blank=True, null=True)
    email = models.CharField(max_length=100)
    telpon = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    
