from django.forms import ModelForm
from django import forms
from .models import *
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
class PrestasiForm(ModelForm):
    class Meta:
         model = Prestasi
         exclude = ['owner']

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
class EkstrakulikulerForm(ModelForm):
    class Meta:
         model = Ekstrakulikuler
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