from aiohttp import request
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from home.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/accounts/')
def index(request):
    return render(request,"index.html")

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
    instance = get_object_or_404(Home, id_home=pk)
    form = HomeForm(req.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/administration/home/')
    task = Home.objects.filter(id_home=pk).first()
    return render(req, 'beranda/update.html', {'form': form, 'data':task}) 
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
    instance = get_object_or_404(Home, id_berita=pk)
    form = BeritaForm(req.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/administration/berita/')
    return render(req, 'berita/update.html', {'form': form}) 
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
    instance = get_object_or_404(Galeri, id_galeri=pk)
    form = GaleriForm(req.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/administration/galeri/')
    return render(req, 'galeri/update.html', {'form': form}) 
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
    instance = get_object_or_404(TentangKami, id_tentangkami=pk)
    form = TentangForm(req.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/administration/tentang/')
    return render(req, 'tentang/update.html', {'form': form}) 
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
    instance = get_object_or_404(Prestasi, id_prestasi=pk)
    form = PrestasiForm(req.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/administration/prestasi/')
    return render(req, 'prestasi/update.html', {'form': form}) 
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
    instance = get_object_or_404(Pendaftaran, id_daftar=pk)
    form = PpdbForm(req.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/administration/ppdb/')
    return render(req, 'ppdb/update.html', {'form': form}) 
@login_required(login_url='/accounts/')
def delete_ppdb(req, pk):
    Pendaftaran.objects.get(id_daftar=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/administration/ppdb/')

@login_required(login_url='/accounts/')
def accountSettings(request):
	profile = request.user
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES,instance=profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/administration/profile/')
	else:
		form = ProfileForm(instance=profile)
		context = {'form':form}
		return render(request, 'profile/index.html', context)