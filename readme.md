
# Новые библиотеки

  ## 1. Faker - создаёт кучу рандочной информации будь то имя возраст email 
  ### Установка **pip install Faker**
  ### Подключение - подключать ничего не надо 
  ### Использование from faker import Faker, faker=Faker(), faker.first_name() - создаёт имя 


  ## 2. Django-guardian - создаёт кучу рандочной информации будь то имя возраст email 
  ### Установка **pip install django-guardian**
  ### Подключение - **INSTALLED_APPS['guardian',]** 
   **AUTHENTICATION_BACKENDS = (**
    **'django.contrib.auth.backends.ModelBackend', # Этот бэкенд Django использует по умолчанию**
    **'guardian.backends.ObjectPermissionBackend', # А это  бэкенд django_guardian)**
  ### Использование from faker import Faker, faker=Faker(), faker.first_name() - создаёт имя 

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