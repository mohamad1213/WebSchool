from aiohttp import request
from django.shortcuts import render, redirect
from .forms import *
from home.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/accounts/')
def index(request):
    return render(request,"index.html")

@login_required(login_url='/accounts/')
def beranda(request):
    tasks = Home.objects.filter(owner=request.user)
    form_input = BeritaForm()
    if request.POST:
        form_input = BeritaForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/home/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'beranda/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })
  
@login_required(login_url='/accounts/')
def galeri(request):
    return render(request,"galeri/index.html")
    
@login_required(login_url='/accounts/')
def tentang(request):
    return render(request,"tentang/index.html")
@login_required(login_url='/accounts/')
def ppdb(request):
    return render(request,"ppdb/index.html")
@login_required(login_url='/accounts/')
def berita(request):
    return render(request,"beranda/index.html")
