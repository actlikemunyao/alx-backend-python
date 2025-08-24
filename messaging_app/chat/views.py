# Simple placeholder view; API not required for CI
from django.http import JsonResponse

def health(request):
    return JsonResponse({'status': 'ok'})
