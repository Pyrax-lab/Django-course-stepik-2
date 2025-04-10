from django.db.models.signals import post_save 
from django.dispatch import receiver 
from django.core.mail import send_mail
from django.urls import reverse
from .models import User1
from .task import send_verification_mail

@receiver(post_save, sender=User1)
def send_verification(sender, instance, created, **kwargs):
    #sender - Модель, которая отправила сигнал
    #instance - Конкретный объект модели,
    #created - Если обьект только что создан
    if created:
        if not instance.is_verifed:
            send_verification_mail(instance.id)
           