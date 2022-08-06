from aiohttp import request
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    home = Home.objects.all()
    berita =Berita.objects.all()
    tentang = TentangKami.objects.all()
    galeri = Galeri.objects.all()
    prestasi = Prestasi.objects.all()
    ppdb = Pendaftaran.objects.all()
    visi = Visimisi.objects.all()
    ukm = Ekstrakulikuler.objects.all()
    context = {
        'home':home,
        'berita':berita,
        'tentang':tentang,
        'visi':visi,
        'galeri':galeri,
        'prestasi':prestasi,
        'ppdb':ppdb,
        'ukm':ukm,
    }
    return render(request,"home.html", context)

def detail_view(request, pk):
    data = Berita.objects.filter(id_berita=pk)
    return render(request,"detail_berita.html", {'berita':data})

def list_berita(request):
    data = Berita.objects.all()
    return render(request,"list_berita.html", {'data':data})

def mi(request):
    return render(request,"mi.html")
def mts(request):
    return render(request,"mts.html")
def ma(request):
    return render(request,"ma.html")