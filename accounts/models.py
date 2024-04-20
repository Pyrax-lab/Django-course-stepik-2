from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser # отличается от AbstractUser тем что в Base нету полей кроме пароля и последний даты входа также на нужно все писать самому авторизацию манаджер  
from django.core.validators import RegexValidator # валидатор регулярных выражений

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Укажите E-mail")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password) # хешируем пароль
        user.save(using=self.db) # сохраняем пользоватлея в бд
        return user 

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
    


    USERNAME_FIELDS = 'email' 
    REQUIRED_FIELDS = [] # обезательные поля при создание модели

    def has_perm(self, perm, obj=None):
        return True 
    
    def has_module(self, app_label=None):
        return True 
    
    @property
    def is_staff(self):
        return self.is_admin
            
    


    













        
            Если бы твоя точка зрения была верна, то мы должны были бы наблюдать [ожидаемый результат], но этого не происходит.» – заставляет оппонента пересмотреть свои выводы.

    «Ты оцениваешь ситуацию в статике, а я говорю о динамике. Важно учитывать изменения со временем.» – идеально, если собеседник игнорирует развитие процессов.

    «Этот аргумент звучит убедительно, но давай разберем, на чем он основан.» – делает тебя рациональным и методичным.

    «Покажи мне данные, подтверждающие твои слова, и я с удовольствием соглашусь.» – работает, если собеседник оперирует неподтвержденными фактами.

    «Ты уверен, что рассматриваешь всю картину целиком, а не только удобную ее часть?» – намекает на предвзятость и заставляет задуматься.

    «Допустим, я приму твою точку зрения. Какой аргумент ты бы привел против нее?» – отличный способ заставить оппонента найти слабые места в своей позиции.

    «Можно ли проверить твое утверждение? Если нет, то как его можно считать объективным?» – мощный аргумент против субъективных мнений.

    «Я не против твоей идеи, я против слабых аргументов в ее защиту.» – демонстрирует, что ты не просто споришь ради спора, а ищешь истину.

    «Если ты не можешь объяснить это простыми словами, значит, сам до конца не понимаешь.» – универсальный прием, особенно если собеседник прячется за сложными терминами.



































