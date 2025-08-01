from django.views.decorators.cache import cache_page
from django.shortcuts import render
from messaging.models import Message
from django.contrib.auth.decorators import login_required

@cache_page(60)
@login_required
def conversation_messages(request):
    messages = Message.objects.filter(receiver=request.user).select_related('sender')
    return render(request, 'chats/messages.html', {'messages': messages})
