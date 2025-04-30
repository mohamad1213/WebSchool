from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from admin1.models import *
from django.shortcuts import render, redirect, get_object_or_404


def Tentang(request):
    context = {
        'tentang':'tentang',
    }
    return render(request,"tentang_kami.html", context)
def index(request):
    home = Home.objects.all()
    article =Article.objects.all().order_by('-created_at')
    tentang = TentangKami.objects.all()
    galeri = Galeri.objects.all()
    prestasi = Prestasi.objects.all()
    ppdb = Pendaftaran.objects.all()
    context = {
        'home':home,
        'article':article[:3],
        'tentang':tentang,
        'galeri':galeri,
        'prestasi':prestasi,
        'ppdb':ppdb,
    }
    return render(request,"home.html", context)
def galeri(request):
    galeri = Galeri.objects.all().order_by('-created_at')
    context={
        "galeri" : galeri
    }
    return render(request, "galeri.html",context)
def prestasi(request):
    prestasi = Prestasi.objects.all().order_by('-created_at')
    context={
        "prestasi_list" : prestasi
    }
    return render(request, "prestasi.html",context)
def detail_prestasi(request, pk):
    prestasi = get_object_or_404(Prestasi, pk=pk)
    related_prestasi = Prestasi.objects.exclude(pk=prestasi.pk)[:3]  # Menampilkan 3 prestasi terkait
    return render(request, 'detail_prestasi.html', {'prestasi': prestasi, 'related_prestasi': related_prestasi})


def detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    related_articles = Article.objects.filter(
        categories__in=article.categories.all()
    ).exclude(pk=article.pk).distinct()[:3]  # Ambil maksimal 3 artikel terkait
    new_artikel = Article.objects.all().order_by('-created_at')
    
    kategori = Category.objects.all()
    return render(request, 'detail_berita.html', {'article': article,'kategori':kategori,'related_articles':related_articles,'new_artikel':new_artikel})
def list_berita(request):
    data = Article.objects.all().order_by('-created_at')
    kategori = Category.objects.all()
    return render(request,"list_berita.html", {'article':data,'kategori':kategori,})

def mi(request):
    return render(request,"mi.html")
def mts(request):
    return render(request,"mts.html")
def ma(request):
    return render(request,"ma.html")