from .models import Pendaftaran

def ppdb_context(request):
    return {
        'has_ppdb': Pendaftaran.objects.exists()
    }
