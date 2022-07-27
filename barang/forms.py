from django.forms import ModelForm
from .models import *

class BarangForms(ModelForm):
    class Meta:
        model = TblBarang
        exclude = []

class CatForms(ModelForm):
    class Meta:
        model = CategoryBrg
        exclude = []

    