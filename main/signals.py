from django.db.models.signals import post_save 
from django.dispatch import receiver 
from django.core.mail import send_mail
from django.urls import reverse
from .models import User1

@receiver(post_save, sender=User1)
def send_email(sender, instance, created, **kwargs):
    #sender - Модель, которая отправила сигнал
    #instance - Конкретный объект модели,
    #created - Усли обьект только что создан
    if created:
        if not instance.is_verifed:
            send_email('Verify your  account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(instance.verification_uuid)}),
            'admin@localhost.ru',
            [instance.email],
            fail_silently=False,)