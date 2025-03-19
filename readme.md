
# Новые библиотеки

  ## 1.Channles - создаёт кучу рандочной информации будь то имя возраст email 
  ### Установка **pip install channels**
  ### Подключение - подключать ничего не надо 
  ### Использование в settings.py добавляем
   **ASGI_APPLICATION = 'django_channels_chat.asgi.application'**


  ## 2. Daphne - это библиотека, которая позволяет назначать права доступа (permissions) на уровне отдельных объектов (Object-level permissions). С её помощью можно задавать разрешения не только для всей модели, но и для конкретных экземпляров (объектов) этой модели.
  ### Установка **pip install daphne**
  ### Подключение - **INSTALLED_APPS['guardian',]** 
   **AUTHENTICATION_BACKENDS = (**
    **'django.contrib.auth.backends.ModelBackend', # Этот бэкенд Django использует по умолчанию**
    **'guardian.backends.ObjectPermissionBackend', # А это  бэкенд django_guardian)**
  ### Использование  **from guardian.admin import GuardedModelAdmin** регистрируем новую модель в админке **class PostAdmin(GuardedModelAdmin): list_display = ('title', )**
  **admin.site.register(Post, PostAdmin)** 
  и теперь в админке можешь для каждого поста добавлять пользователей которые будут имень выставленные разрешения

   ## 3. Channels Redis - это бэкенд для Django Сhannels который использует Redis как message broker (посредник) для передачи сообщений между процессами.
   ### Установка **pip install channels-redis**
   ### Подключение - **CHANNEL_LAYERS = {**
  **"default": {**
        **'BACKEND': "channels_redis.core.RedisChannelLayer",**
        **'CONFIG': {"hosts": ['redis://127.0.0.1:6379',]},}}** тут мы подключаемся к серверу !НО перед этим сервер redis должен быть запущен как проверить в cmd пишем redis-cli ping если получаем PONG все ок если нет тогда запускаем сервер сами для жтого пишем redis-server и все! 
   ### Использование - везде где есть **self.channel_layer.group_send** мы автоматически работаем с redis 

