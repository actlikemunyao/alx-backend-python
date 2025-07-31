import logging
import time
from datetime import datetime
from django.http import HttpResponseForbidden, JsonResponse
from collections import defaultdict

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(filename='requests.log', level=logging.INFO)

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_entry = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_entry)
        return self.get_response(request)

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now().time()
        if request.path.startswith('/chats') and (now.hour < 18 or now.hour >= 21):
            return HttpResponseForbidden("Access to chat is restricted at this time.")
        return self.get_response(request)

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_message_log = defaultdict(list)

    def __call__(self, request):
        if request.method == "POST" and request.path.startswith('/chats'):
            ip = request.META.get('REMOTE_ADDR')
            now = time.time()
            self.ip_message_log[ip] = [t for t in self.ip_message_log[ip] if now - t < 60]
            if len(self.ip_message_log[ip]) >= 5:
                return JsonResponse({'error': 'Rate limit exceeded'}, status=429)
            self.ip_message_log[ip].append(now)
        return self.get_response(request)

class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/chats') and request.method in ['POST', 'DELETE']:
            if not request.user.is_authenticated or getattr(request.user, 'role', None) not in ['admin', 'moderator']:
                return JsonResponse({'error': 'Permission denied'}, status=403)
        return self.get_response(request)
        ["class RolepermissionMiddleware"]
