
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

   ## 3. Rosseta - библиотека для удобного перевода текстов с графическим интрефейсом 
   ### Установка **pip install django-rosetta**
   ### Подключение - **path("rosetta/", include('rosetta.urls')) # rosetta** в главный urls подключаем либу
   ### Использование - заходим по адресу "rosetta/ и попадаем в графическую оболочку. С данной либой можно не лезть в файлы проекта locale а сразу на сайте все перенводы настроить

