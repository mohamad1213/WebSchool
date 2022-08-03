from django.forms import ModelForm
from .models import *
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['username', 'password1']


class HomeForm(ModelForm):
    class Meta:
         model = Home
         exclude = ['owner']
class BeritaForm(ModelForm):
    class Meta:
         model = Berita
         exclude = ['owner']
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

class ProfileForm(ModelForm):
    class Meta:
         model = Profile
         exclude = ['user']