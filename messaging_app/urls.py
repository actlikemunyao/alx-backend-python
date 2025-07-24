 ["from django.urls import", "path", "include", "routers.DefaultRouter()"]
["NestedDefaultRouter", "ConversationViewSet", "MessageViewSet"]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),  # 👈 include your app's routes under /api/
]
