# Чистый онлайн чат на WebSocket

# Новые библиотеки

  ## 1.Channles - это библиотека для работы с асинхроностью и вебсокетами 
  ### Установка **pip install channels**
  ### Подключение, Использование - 
    1**INSTALLED_APPS = ['channels', 'daphne',]**

    2**ASGI_APPLICATION = 'django_chat.asgi.application'**

    3**websocket_urlpatterns = [path('', Test.as_asgi()),]** создаём новый файл routing.py и там будем записывать все вебсокет маршруты
  
    4**class Test(WebsocketConsumer): def connect(self): self.accept()**  создаём новый файл consumers.py и там будут содержатся наши типо виюхb только для вебсокетов self.accept() принимает подключение
  
    5**application = ProtocolTypeRouter({**
    **"http": asgi_application,** это наши стандартные url-ы для обычного http 
    **"websocket": "websocket": URLRouter(chat.routing.websocket_urlpatterns)})** самый просто способ добавление маршрутов для вебсокетов
  
    6**CHANNEL_LAYERS = {}** можно использовать если это нужно например как у нас веб чат используется код вместе с channels-redis
  


  ## 2. Daphne - это ASGI сервер для работы с websocket + асинхрон
  ### Установка **pip install daphne**
  ### Подключение - 
  
    1**INSTALLED_APPS['daphne',]** 
  
    2**ASGI_APPLICATION = 'django_chat.asgi.application'**
  ### Использование  **manage.py runserver** он сам заменится на Daphne
  


  ## 3. Channels Redis - это бэкенд для Django Сhannels который использует Redis как message broker (посредник) для передачи сообщений между процессами.
  ### Установка **pip install channels-redis**
  ### Подключение -   
    **CHANNEL_LAYERS = {**
    **"default": {**
        **'BACKEND': "channels_redis.core.RedisChannelLayer",**
        **'CONFIG': {"hosts": ['redis://127.0.0.1:6379',]},}}** тут мы подключаемся к серверу !НО перед этим сервер redis должен быть запущен как проверить в cmd пишем redis-cli ping если получаем PONG все ок если нет тогда запускаем сервер сами для жтого пишем redis-server и все! 
  ### Использование - везде где есть **self.channel_layer.group_send** мы автоматически работаем с redis 

