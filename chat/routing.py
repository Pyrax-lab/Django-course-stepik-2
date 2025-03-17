from django.urls import path, re_path 
from .consumers import JoinAndLeave, GroupConsumer


websocket_urlpatterns = [ # 4 шаг добавляем пути 
    path('', JoinAndLeave.as_asgi()),
    path('groups/<uuid:uuid>/', GroupConsumer.as_asgi())
]