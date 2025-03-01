from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser # отличается от AbstractUser тем что в Base нету полей кроме пароля и последний даты входа также на нужно все писать самому авторизацию манаджер  
from django.core.validators import RegexValidator # валидатор регулярных выражений

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Укажите E-mail")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password) # хешируем пароль
        user.save(using=self._db) # сохраняем пользоватлея в бд
        return user 
    
    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user 


# AUTH_USER_MODEL = 'accounts.User' нужно добавить в settings для того чтобы использовать нашу модель
# чтобы потом использовать науш созданную модель в проекте нужно исмпортировать настройки из from django.conf import settings и потом settings.AUTH_USER_MODEL
class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    is_staff = models.BooleanField(default=False) 
    is_activ = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    phone_regex = RegexValidator(regex=r"^((\+7)|8)\d{10}$", message='Enter phone must be enterned in the format "+078700420"')
    phone_number = models.CharField(validators=[phone_regex], max_length=9, null=True, blank=True) 

    def __str__(self):
        return self.email 
    


    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = [] # обезательные поля при создание модели!

    def has_perm(self, perm, obj=None):
        return True 
    
    def has_module(self, app_label=None):
        return True 
    
    @property
    def is_staff(self):
        return self.is_admin
            
    
    objects = CustomUserManager()

    



