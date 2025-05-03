from .models import Pendaftaran
from .models import Home

def ppdb_context(request):
    return {
        'has_ppdb': Pendaftaran.objects.exists()
    }

def home_logo(request):
    try:
        u = Home.objects.first()
    except Home.DoesNotExist:
        u = None
    return {'u': u}
