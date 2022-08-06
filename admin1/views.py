from aiohttp import request
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from home.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os

@login_required(login_url='/accounts/')
def index(request):
    data = Profile.objects.all()
    context ={'data':data}
    return render(request,"index.html", context)
@login_required(login_url='/accounts/')
def box(request):
    return render(request,"boxicon.html")
#Beranda 
@login_required(login_url='/accounts/')
def beranda(request):
    tasks = Home.objects.filter(owner=request.user)
    form_input = HomeForm()
    if request.POST:
        form_input = HomeForm(request.POST, request.FILES)
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
def update_beranda(req, pk):
    instance = Home.objects.get(id_home=pk)
    if req.POST:
        if len(req.FILES) != 0:
            if len(instance.logo) > 0:
                os.remove(instance.logo.path)
            instance.logo = req.FILES['logo']
        instance.h1 = req.POST.get('h1')
        instance.nama_pondok = req.POST.get('nama_pondok')
        instance.alamat = req.POST.get('alamat')
        instance.telpon = req.POST.get('telpon')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/home/')
    context = {"data":instance}
    return render(req, 'beranda/update.html', context) 

@login_required(login_url='/accounts/')
def delete_beranda(req, pk):
    Home.objects.get(id_home=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/home/')

##Berita
@login_required(login_url='/accounts/')
def berita(request):
    tasks = Berita.objects.filter(owner=request.user)
    form_input = BeritaForm()
    if request.POST:
        form_input = BeritaForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/berita/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'berita/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })
@login_required(login_url='/accounts/')
def update_berita(req, pk):
    instance = Berita.objects.get(id_berita=pk)
    if req.POST:
        if len(req.FILES) != 0:
            if len(instance.image) > 0:
                os.remove(instance.image.path)
            instance.image = req.FILES['image']
        instance.nama_penulis = req.POST.get('nama_penulis')
        instance.judul = req.POST.get('judul')
        instance.isi = req.POST.get('isi')
        instance.penerbit = req.POST.get('penerbit')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/berita/')
    context = {"data":instance} 
    return render(req, 'berita/update.html', context) 
    
@login_required(login_url='/accounts/')
def delete_berita(req, pk):
    Berita.objects.get(id_berita=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/berita/')

#####Galeri
@login_required(login_url='/accounts/')
def galeri(request):
    tasks = Galeri.objects.filter(owner=request.user)
    form_input = GaleriForm()
    if request.POST:
        form_input = GaleriForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/galeri/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'galeri/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })
@login_required(login_url='/accounts/')
def update_galeri(req, pk):
    instance = Galeri.objects.get(id_galeri=pk)
    if req.POST:
        if len(req.FILES) != 0:
            if len(instance.image) > 0:
                os.remove(instance.image.path)
            instance.image = req.FILES['image']
        instance.desc = req.POST.get('desc')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/galeri/')
    context = {"data":instance}
    return render(req, 'galeri/update.html', context) 
@login_required(login_url='/accounts/')
def delete_galeri(req, pk):
    Galeri.objects.get(id_galeri=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/galeri/')
    
##Tentang
@login_required(login_url='/accounts/')
def tentang(request):
    tasks = TentangKami.objects.filter(owner=request.user)
    form_input = TentangForm()
    if request.POST:
        form_input = TentangForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/tentang/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'tentang/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })
@login_required(login_url='/accounts/')
def update_tentang(req, pk):
    instance = TentangKami.objects.get(id_tentangkami=pk)
    if req.POST:
        if len(req.FILES) != 0:
            if len(instance.image) > 0:
                os.remove(instance.image.path)
            instance.image = req.FILES['image']
        instance.nama_pengasuh = req.POST.get('nama_pengasuh')
        instance.desc = req.POST.get('desc')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/tentang/')
    context = {"data":instance} 
    return render(req, 'tentang/update.html', context) 
@login_required(login_url='/accounts/')
def delete_tentang(req, pk):
    TentangKami.objects.get(id_tentangkami=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/tentang/')

##Prestasi
@login_required(login_url='/accounts/')
def prestasi(request):
    tasks = Prestasi.objects.filter(owner=request.user)
    form_input = PrestasiForm()
    if request.POST:
        form_input = PrestasiForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/prestasi/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'prestasi/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })
@login_required(login_url='/accounts/')
def update_prestasi(req, pk):
    instance = Prestasi.objects.get(id_prestasi=pk)
    if req.POST:
        if len(req.FILES) != 0:
            if len(instance.image) > 0:
                os.remove(instance.image.path)
            instance.image = req.FILES['image']
        instance.desc = req.POST.get('desc')
        instance.nama = req.POST.get('nama')
        instance.lokasi = req.POST.get('lokasi')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/prestasi/')
    context = {"data":instance}
    return render(req, 'prestasi/update.html', context) 
@login_required(login_url='/accounts/')
def delete_prestasi(req, pk):
    Prestasi.objects.get(id_prestasi=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/prestasi/')

##PPDB
@login_required(login_url='/accounts/')
def ppdb(request):
    tasks = Pendaftaran.objects.filter(owner=request.user)
    form_input = PpdbForm()
    if request.POST:
        form_input = PpdbForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/ppdb/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'ppdb/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })
@login_required(login_url='/accounts/')
def update_ppdb(req, pk):
    instance = Pendaftaran.objects.get(id_daftar=pk)
    if req.POST:
        if len(req.FILES) != 0:
            if len(instance.brosur) > 0:
                os.remove(instance.brosur.path)
            instance.brosur = req.FILES['brosur']
        instance.email = req.POST.get('email')
        instance.telpon = req.POST.get('telpon')
        instance.lokasi = req.POST.get('lokasi')
        instance.link_daftar = req.POST.get('link_daftar')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/ppdb/')
    context = {"data":instance}
    return render(req, 'ppdb/update.html', context)
@login_required(login_url='/accounts/')
def delete_ppdb(req, pk):
    Pendaftaran.objects.get(id_daftar=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/ppdb/')

##UKM
@login_required(login_url='/accounts/')
def ukm(request):
    tasks = Ekstrakulikuler.objects.filter(owner=request.user)
    form_input = EkstrakulikulerForm()
    if request.POST:
        form_input = EkstrakulikulerForm(request.POST)
        if form_input.is_valid():
            form_input.instance.owner = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/ukm/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'ukm/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })
@login_required(login_url='/accounts/')
def update_ukm(req, pk):
    instance = Ekstrakulikuler.objects.get(id_ekstra=pk)
    if req.POST:
        instance.nama_ekstra = req.POST.get('nama_ekstra')
        instance.desc = req.POST.get('desc')
        instance.icon = req.POST.get('icon')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/ukm/')
    context = {"data":instance}
    return render(req, 'ukm/update.html', context)
@login_required(login_url='/accounts/')
def delete_ukm(req, pk):
    Ekstrakulikuler.objects.get(id_ekstra=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/ukm/')

@login_required(login_url='/accounts/')
def accountSettings(req, pk):
    instance = Profile.objects.get(id=pk)
    if req.POST:
        if len(req.FILES) != 0:
            if len(instance.profile_pic) > 0:
                os.remove(instance.profile_pic.path)
            instance.profile_pic = req.FILES['profile_pic']
        instance.name = req.POST.get('name')
        instance.phone = req.POST.get('phone')
        instance.email = req.POST.get('email')
        instance.alamat = req.POST.get('alamat')
        instance.save()
        messages.success(req, "data Telah ditambahkan")
        return redirect('/administration/profile/')
    context = {"data":instance}
    return render(req, 'profile/update.html', context)

@login_required(login_url='/accounts/')
def profile(req):
    data = Profile.objects.all()
    return render(req, 'profile/index.html', {'data': data})
