from django.shortcuts import render
from .models import User1 
# Create your views here.




def verifid(reqeust, uuid):
    try: 
        user = User1.objects.get(verfication_uuid = uuid, is_verifed=False)
    except User1.DoesNotExist:
        print("user does note exists")

    user.is_verifed = True 
    user.save()
    return render(reqeust, 'activate.html')