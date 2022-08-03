from aiohttp import request
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    data = Home.objects.all()
    return render(request,"home.html", {'data':data})

def detail_view(request, id):
    data = Berita.objects.filter(id_berita=id)
    return render(request,"detail_berita.html", {'data':data})

def mi(request):
    return render(request,"mi.html")
def mts(request):
    return render(request,"mts.html")
def ma(request):
    return render(request,"ma.html")