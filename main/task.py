from django.urls import reverse 
from django.core.mail import send_mail
from .models import User1 
from publish.celery import app 


@app.task 
def send_verification_mail(user_id: int):
    try : 
        user = User1.objects.get(id = user_id)
        send_mail(  # ✅ теперь вызывается Django send_mail
                'Verify your account',
                'Follow this link to verify your account: '
                'http://localhost:8000%s' % reverse('verifid', kwargs={'uuid': str(user.verfication_uuid)}),
                'admin@localhost.ru',
                [user.email],
                fail_silently=False,
            )
    except User1.DoesNotExist:
        print('User does not exists')