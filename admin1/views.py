from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
# views.py
from django.http import JsonResponse
from django.db.models.functions import TruncDate
from django.db.models import Count
from .models import SiteVisit
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from home.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from admin1.forms import ProfileForm, form_validation_error
from django.views.generic import View
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from .forms import GeneratePromptForm, ArticleForm
from .models import Article
import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FAQ
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GeneratePromptForm
from .models import *
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
import json
import markdown
from .utils import *

def visimisi_list(request):
    visimisi = VisiMisi.objects.all().order_by('-created_at')
    return render(request, 'visimisi/index.html', {'visimisi': visimisi})

def visimisiCreate(request):
    instance = VisiMisi.objects.first()  # Ambil data pertama
    if request.method == 'POST':
        form = VisiMisiForms(request.POST, instance=instance)
        if form.is_valid():
            visimisi = form.save(commit=False)
            visimisi.owner = request.user
            visimisi.save()
            form.save()
            return redirect('administration:visimisi_list')  # Ubah ke nama URL yang sesuai
    else:
        form = VisiMisiForms(instance=instance)

    return render(request, 'visimisi/create.html', {'form': form})
def tentang_list(request):
    tentang_kami = TentangKami2.objects.all().order_by('-created_at')
    return render(request, 'tentangkami/index.html', {'tentang_kami': tentang_kami})

def TentangKamiCreate(request):
    instance = TentangKami2.objects.first()  # Ambil data pertama
    if request.method == 'POST':
        form = TentangKamiForms(request.POST, instance=instance)
        if form.is_valid():
            tentang_kami = form.save(commit=False)
            tentang_kami.owner = request.user
            tentang_kami.save()
            form.save()
            return redirect('administration:tentang_list')  # Ubah ke nama URL yang sesuai
    else:
        form = TentangKamiForms(instance=instance)

    return render(request, 'tentangkami/create.html', {'form': form})
@csrf_exempt
def generate_keywords(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        topic = data.get('topic', '')
        if topic:
            # Di sini kamu bisa pakai fungsi AI atau rule-based untuk generate keyword
            keywords = ai_generate_keywords(topic)  # Buat fungsi ini
            return JsonResponse({'keywords': ', '.join(keywords)})
    return JsonResponse({'keywords': ''})
def generate_article(request):
    if request.method == 'POST':
        form = SEOArticleForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            keywords = form.cleaned_data['keywords']
            language = form.cleaned_data['language']
            length = form.cleaned_data['length']

            keyword_str = ', '.join(keywords.split(','))
            prompt = (
                f"Tulis artikel SEO lengkap dalam bahasa {language} tentang '{topic}'.\n"
                f"Jumlah paragraf: {length}.\n"
                f"Sisipkan kata kunci: {keyword_str}.\n"
                f"Gunakan struktur SEO: Judul (H1), Meta Description, subjudul (H2), bullet point, dan kesimpulan.\n"
                f"Tulis dengan gaya profesional dan mudah dipahami."
            )

            content = gemini_generate_content(prompt)
            content = markdown.markdown(content)

            artikel = Article.objects.create(title=topic, content=content)
            return redirect('administration:article_editor', artikel.id)
    else:
        form = SEOArticleForm()

    return render(request, 'artikel/generate_artikel.html', {'form': form})
def edit_artikel(request, pk):
    artikel = get_object_or_404(Article, id=pk)
    if request.method == 'POST':
        form = ArticleEditForm(request.POST or None, request.FILES, instance=artikel)
        if form.is_valid():
            form.save()
            return redirect('administration:article_list')
    else:
        form = ArticleForm(instance=artikel)

    return render(request, 'artikel/edit_artikel.html', {
        'form': form,
        'artikel': artikel
    })

def preview_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'artikel/preview_article.html', {'article': article})

def save_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Artikel berhasil dipublikasikan!")
            return redirect('administration:article_list')
    # Tambahkan ini untuk kasus jika bukan POST atau form tidak valid
    return redirect('administration:article_editor', pk=article.pk)

def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'artikel/artikel_list.html', {'articles': articles})
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    model = Profile

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)
    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'profile/index.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)
        if form.is_valid():
            form.instance.user=request.user
            form.get_avatar = request.FILES['profile_pic']
            profile = form.save()
            img_object = form.instance  
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Data berhasil ditambahkan')
            messages.error(request, form_validation_error(form))
        return redirect('/administration/profile/') 

def chart_data(request):
    visits = (
        SiteVisit.objects
        .annotate(date=TruncDate('timestamp'))
        .values('date')
        .annotate(total=Count('id'))
        .order_by('date')
    )
    data = {
        'labels': [v['date'].strftime('%Y-%m-%d') for v in visits],
        'totals': [v['total'] for v in visits]
    }
    return JsonResponse(data)


@login_required(login_url='/accounts/')
def index(request):
    data = Profile.objects.all()
    artikel = Article.objects.all()
    galeri = Galeri.objects.all()
    data = Profile.objects.all()
    data = Profile.objects.all()
    context ={
        'galeri':galeri,
        'artikel':artikel,
        'data':data,
              
              }
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
def prestasiCreate(request):
    if request.method == 'POST':
        form = PrestasiForm(request.POST, request.FILES)
        if form.is_valid():
            prestasi = form.save(commit=False)
            prestasi.owner = request.user
            prestasi.save()
            form.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('administration:prestasi')  # Ubah ke nama URL yang sesuai
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form.errors)
    else:
        form = PrestasiForm()

    return render(request, 'prestasi/create.html', {'form': form})
@login_required(login_url='/accounts/')
def prestasi(request):
    tasks = Prestasi.objects.filter(owner=request.user)
    return render(request, 'prestasi/index.html',{
        'data': tasks,
        
    })
@login_required(login_url='/accounts/')
def update_prestasi(req, pk):
    instance = Prestasi.objects.get(id=pk)
    if req.POST:
        instance.image = req.FILES['image']
        instance.content = req.POST.get('content')
        instance.slug = req.POST.get('slug')
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
def profile(request):
    tasks = Profile.objects.filter(user=request.user)
    form_input = ProfileForm()
    if request.POST:
        form_input = ProfileForm(request.POST, request.FILES)
        if form_input.is_valid():
            form_input.instance.user = request.user
            form_input.save()
            messages.success(request, 'Data telah ditambahkan.')
            return redirect('/administration/profile/')
        else:
            messages.error(request, 'A problem has been occurred while submitting your data.')
            print(form_input.errors)
    return render(request, 'profile/index.html',{
        'form' : form_input,
        'data': tasks,
        
    })
