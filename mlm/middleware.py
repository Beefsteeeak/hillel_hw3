import re

from django.utils import timezone

from .models import Log


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not re.search('/admin/', request.path):
            Log.objects.create(path=request.path, method=request.method, timestamp=timezone.now())
        response = self.get_response(request)
        return response
