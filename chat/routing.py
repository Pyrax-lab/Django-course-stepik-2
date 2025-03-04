from django.urls import path, re_path 
from .consumers import JoinAndLeave


websocket_urlpatterns = [
    path('', JoinAndLeave.as_asgi())
]