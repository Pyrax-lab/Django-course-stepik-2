from django.urls import path, re_path 
from .consumers import JoinAndLeave


websocket_urlpatterns = [ # 4 шаг добавляем пути 
    path('', JoinAndLeave.as_asgi())
]