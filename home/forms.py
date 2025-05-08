from django.forms import ModelForm
from .models import *
from django import forms
from home.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class LoginForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['username', 'password1']

class ImageForm(ModelForm):
    class Meta:
         model = Home
         fields = ['logo']


class SantriPendaftarForm(forms.ModelForm):
    class Meta:
        model = SantriPendaftar
        fields = [
            'nama', 'nisn', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin',
            'no_hp', 'email', 'nama_ayah', 'nama_ibu', 'alamat', 'foto'
        ]
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama lengkap'}),
            'nisn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan NISN'}),
            'tempat_lahir': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan tempat lahir'}),
            'tanggal_lahir': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'jenis_kelamin': forms.Select(attrs={'class': 'form-select'}),
            'no_hp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan no HP'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan email'}),
            'nama_ayah': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama ayah'}),
            'nama_ibu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama ibu'}),
            'alamat': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan alamat lengkap',
                'rows': 2
            }),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

