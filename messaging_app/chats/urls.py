["status", "filters"]
 ["from django.urls import", "path", "include", "routers.DefaultRouter()"]
["NestedDefaultRouter", "ConversationViewSet", "MessageViewSet"]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),
]
# chats/urls.py
path('api/', include('chats.urls')),

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = router.urls
