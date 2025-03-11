"""
ASGI config for django_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
import chat.routing

from channels.routing import ProtocolTypeRouter, URLRouter 
from channels.security.websocket import AllowedHostsOriginValidator # Блокирует WebSocket-подключения, которые приходят с доменов, не указанных в ALLOWED_HOSTS Django, защита от cors-атак
from channels.auth import AuthMiddlewareStack # Добавляет механизм аутентификации позволяет работать с пользователем self.scope['user'] аналог request.user
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat.settings')

asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": asgi_application,# это наши стандартные url-ы 
    "websocket": AllowedHostsOriginValidator( # Защита от атак 6 шаг добавляем пути именно для вебсокетов
                 AuthMiddlewareStack(
                 URLRouter(chat.routing.websocket_urlpatterns)))
    #"websocket": URLRouter(chat.routing.websocket_urlpatterns) самый просто способ добавление маршрутов для вебсокетов
})
