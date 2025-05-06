# middleware.py (buat file baru)
from .models import SiteVisit
from django.utils.deprecation import MiddlewareMixin

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        SiteVisit.objects.create(ip_address=ip)
