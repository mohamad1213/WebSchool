from .models import Pendaftaran
from .models import Home


def ppdb_context(request):
    daftar_list = Pendaftaran.objects.all()
    return {
        'has_ppdb': daftar_list.exists(),
        'ppdb_list': daftar_list
    }

def home_logo(request):
    try:
        u = Home.objects.first()
    except Home.DoesNotExist:
        u = None
    return {'u': u}
