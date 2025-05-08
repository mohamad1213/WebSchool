from django.forms import ModelForm
from django import forms
from .models import *
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article
from django import forms
from .models import Article
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class TentangKamiForms(forms.ModelForm):
    class Meta:
        model = TentangKami2
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': CKEditorUploadingWidget(),
            
        }
class VisiMisiForms(forms.ModelForm):
    class Meta:
        model = VisiMisi
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': CKEditorUploadingWidget(),
            
        }
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'categories', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'content': CKEditorUploadingWidget(),
            
        }
class SEOArticleForm(forms.Form):
    topic = forms.CharField(
        label="Topik Artikel",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan topik artikel'})
    )
    keywords = forms.CharField(
        label="Kata Kunci",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Contoh: Romadhon, Puasa, Takjil'})
    )
    language = forms.ChoiceField(
        label="Bahasa",
        choices=[('Indonesia', 'Indonesia'), ('English', 'English'), ('French', 'French')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    length = forms.IntegerField(
        label="Jumlah Paragraf",
        min_value=1,
        max_value=20,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'categories', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'content': CKEditorUploadingWidget(),
            
        }
class GeneratePromptForm(forms.Form):
    tema = forms.CharField(label='Tema Artikel', max_length=200)

class LoginForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['username', 'password1']

def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg
class HomeForm(ModelForm):
    class Meta:
         model = Home
         exclude = ['owner']
class BeritaForm(ModelForm):
    class Meta:
         model = Berita
         exclude = ['owner','desc']
class PrestasiForm(forms.ModelForm):
    class Meta:
        model = Prestasi
        fields = ['nama', 'lokasi','content', 'image','slug']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'lokasi': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'content': CKEditorUploadingWidget(),
            
        }
        

class TentangForm(ModelForm):
    class Meta:
         model = TentangKami
         exclude = ['owner']
class GaleriForm(ModelForm):
    class Meta:
         model = Galeri
         exclude = ['owner']
class PpdbForm(ModelForm):
    class Meta:
         model = Pendaftaran
         exclude = ['owner']

class ProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=255)
	last_name = forms.CharField(max_length=255)
	email = forms.EmailField()	

	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']

class EditProfileForm(ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    phone = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    alamat = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio','phone','alamat']
        
from django import forms
from home.models import DataLengkapSantri

class DataLengkapSantriForm(forms.ModelForm):
    class Meta:
        model = DataLengkapSantri
        fields = [
            'asal_sekolah',
            'no_ijazah',
            'golongan_darah',
            'riwayat_penyakit',
            'berat_badan',
            'tinggi_badan',
            'kebutuhan_khusus',
            'nama_wali',
            'hubungan_wali',
            'no_hp_wali',
            'penerima_kps',
            'no_kps',
            'upload_kk',
            'upload_akte'
        ]
        widgets = {
            'asal_sekolah': forms.TextInput(attrs={'class': 'form-control'}),
            'no_ijazah': forms.TextInput(attrs={'class': 'form-control'}),
            'golongan_darah': forms.Select(attrs={'class': 'form-control'}),
            'riwayat_penyakit': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'berat_badan': forms.NumberInput(attrs={'class': 'form-control'}),
            'tinggi_badan': forms.NumberInput(attrs={'class': 'form-control'}),
            'kebutuhan_khusus': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_wali': forms.TextInput(attrs={'class': 'form-control'}),
            'hubungan_wali': forms.TextInput(attrs={'class': 'form-control'}),
            'no_hp_wali': forms.TextInput(attrs={'class': 'form-control'}),
            'penerima_kps': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'no_kps': forms.TextInput(attrs={'class': 'form-control'}),
            'upload_kk': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'upload_akte': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
