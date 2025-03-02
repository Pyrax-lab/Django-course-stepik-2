from django.db import models
from django.contrib.auth import get_user_model 
from uuid import uuid4 
from django.urls import reverse

User = get_user_model() # будем всегда уверены что мы используем именно нашу модель пользоватея AbstractBaseUser


class Group(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(User)

    def __str__(self):
        return f"Group {self.name}-{self.uuid}"
    
    def get_absolute_url(self):
        return reverse("group", args=[str(self.uuid)])
    
    def add_user_to_group(self, user):
        self.members.add(user)
        self.event_set.create(type='Join', user=user) # или же можно написать по простому Event.objects.create(type='Join', user=user)
        self.save()     

    def remove_user_from_group(self, user):
        self.members.remove(user)
        self.event_set.create(type='Left', user=user)
        self.save()

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timenow = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name = "mesage_moster")

    def __str__(self):
        return f"{self.author}:- {self.content} @{self.timenow}"
    

class Event(models.Model):
    CHOICES = [('Join', 'join'), ('Left', 'left')]
    type = models.CharField(choices=CHOICES , max_length=10)
    description = models.TextField(help_text="A description of the event", max_length=150, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timenow = models.DateTimeField(auto_now_add = True)
    group  = models.ForeignKey(Group, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.description=f"{self.user} {self.type} the {self.group.name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description