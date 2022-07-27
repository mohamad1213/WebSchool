from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
@login_required(login_url='/accounts/')
def barang(request):
    data = TblBarang.objects.all()
    form_barang = BarangForms()
    if request.method == 'POST':
        barang = BarangForms(request.POST)
        if barang.is_valid():
            barang.save()
            return redirect('/')
        else:
            return HttpResponse("SomethingWrong")  
    else:
        return render(request, 'barang/barang.html', {'data':data,'form':form_barang})

@login_required(login_url='/accounts/')
def create_barang(request):
    form_barang = BarangForms()
    if request.method == 'POST':
        barang = BarangForms(request.POST)
        if barang.is_valid():
            barang.save()
            return redirect('/barang/')
        else:
            return HttpResponse("SomethingWrong")  
    else:
        return render(request, 'barang/create_barang.html', {'form':form_barang})

@login_required(login_url='/accounts/')
def detail_barang(req, pk):
    detail_barang = TblBarang.objects.filter(id_barang=pk).first()
    return render(req, 'barang/barang_detail.html', {
        'data': detail_barang,
    })

@login_required(login_url='/accounts/')
def delete_barang(req, pk):
    TblBarang.objects.get(id_barang=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/barang')

@login_required(login_url='/accounts/')
def update_barang(req, pk):
    instance = get_object_or_404(TblBarang, id_barang=pk)
    form = BarangForms(req.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/barang')
    return render(req, 'barang/barang_update.html', {'form': form}) 
    
@login_required(login_url='/accounts/')
def Category(request):
    data = CategoryBrg.objects.all()
    form_category = CatForms()
    if request.method == 'POST':
        category = CatForms(request.POST)
        if category.is_valid():
            category.save()
            return redirect('category')
        else:
            return HttpResponse("SomethingWrong")  
    return render(request, 'category/category.html', {'data':data,'form':form_category})

@login_required(login_url='/accounts/')
def delete_category(req, pk):
    CategoryBrg.objects.get(id_cat=pk).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/category')

@login_required(login_url='/accounts/')
def update_category(req, pk):
    instance = get_object_or_404(CategoryBrg, id_cat=pk)
    form = CatForms(req.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/category')
    return render(req, 'category/category_update.html', {'form': form})
    
