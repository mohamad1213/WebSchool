from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from admin1.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import detect_intent_texts  # Fungsi yang Anda buat sebelumnya
import uuid
import json
import uuid
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.cloud import dialogflow_v2 as dialogflow
from django.http import JsonResponse
from google.cloud import dialogflow_v2 as dialogflow
from google.oauth2 import service_account


def daftar_santri(request):
    if request.method == 'POST':
        form = SantriPendaftarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('daftar_berhasil')
    else:
        form = SantriPendaftarForm()
    return render(request, 'pendaftaran/formulir.html', {'form': form})
# Ganti dengan project ID Anda
PROJECT_ID = "newagent-ilgg"
LANGUAGE_CODE = "id"
CREDENTIAL_PATH = r"C:\Users\LENOVO X1\Downloads\Websekolah\pos\credentials3.json"
credentials = service_account.Credentials.from_service_account_file(CREDENTIAL_PATH)

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        user_message = data.get('message')

        # Konfigurasi Session Client
        session_client = dialogflow.SessionsClient(credentials=credentials)

        PROJECT_ID = 'newagent-ilgg'  # Ganti dengan ID agent kamu
        SESSION_ID = str(uuid.uuid4())
        session = session_client.session_path(PROJECT_ID, SESSION_ID)

        text_input = dialogflow.TextInput(text=user_message, language_code='id')
        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        reply = response.query_result.fulfillment_text
        return JsonResponse({'reply': reply})

def detect_intent_text(text, session_id):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=LANGUAGE_CODE)
    query_input = dialogflow.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        return response.query_result.fulfillment_text
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"
    
def visimisi(request):
    visimisi = VisiMisi.objects.all()
    context = {
        'visimisi':visimisi,
    }
    return render(request,"visimisi.html", context)
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