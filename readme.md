
# Новые библиотеки

  ## 1. Faker - создаёт кучу рандочной информации будь то имя возраст email 
  ### Установка **pip install Faker**
  ### Подключение - подключать ничего не надо 
  ### Использование from faker import Faker, faker=Faker(), faker.first_name() - создаёт имя 


  ## 2. Django-guardian - это библиотека, которая позволяет назначать права доступа (permissions) на уровне отдельных объектов (Object-level permissions). С её помощью можно задавать разрешения не только для всей модели, но и для конкретных экземпляров (объектов) этой модели.
  ### Установка **pip install django-guardian**
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


   ## 3.sorl-thumbnail - это Django-приложение, которое помогает автоматически создавать уменьшенные версии изображений (миниатюры) и кешировать их для быстрого отображения.
   ### Установка **pip install sorl-thumbnail**
   ### Подключение - **INSTALLED_APPS['sorl.thumbnail']** в INSTALLED_APPS добаляем либу
   ### Использование - допустим у нас в модели есть картика **image = models.ImageField(uploadt_to='images/')**
   **{% load thumbnail %}**#В шаблоне нужно подключить 
   **<img src="{% thumbnail product.image 200x200 crop %}" alt="Thumbnail">** оборачиваем в специальынй тег thumbnail

# Новые Темы 

  ## Index в базе данных 
  ### 1. B-Tree Index (BtreeIndex)- Это стандартный индекс, используемый по умолчанию.
  Данные хранятся в виде сбалансированного дерева (B-Tree), где каждая операция поиска, вставки и удаления выполняется за O(log n).

  *Код - к полю добавить **,db_index=True**
  
  🔹 Когда использовать?
  - ✅ Для точного поиска (WHERE column = 'value')
  - ✅ Для диапазонного поиска (WHERE column > 10 AND column < 100)
  - ✅ Для сортировки (ORDER BY column ASC/DESC)

  ⚠️ Когда НЕ подходит?
  - ❌ Медленный при полнотекстовом поиске.
  - ❌ Неэффективен для сложных геометрических запросов.

  ### 2. Hash Index (HashIndex) - Хранит хэш-коды значений, а не сами значения.
  
  *Код - импортировать `from django.contrib.postgres.indexes import HashIndex`
  `class Meta:`
    `indexes = (HashIndex(fields=('first_name',),name="hr_%(class)s_about_ix",),)`
  
  Идеален для точного поиска (WHERE column = 'value').
  Работает быстрее B-Tree ПРИ ТОЧНОМ ПОИСКЕ.

  🔹 Когда использовать?
  
  - ✅ Только для точного поиска (WHERE column = 'value').

  ⚠️ Когда НЕ подходит?
  - ❌ НЕ поддерживает диапазонные запросы (>, <, BETWEEN).
  - ❌ НЕ поддерживает сортировку (ORDER BY).
  - ❌ Используется только в PostgreSQL.