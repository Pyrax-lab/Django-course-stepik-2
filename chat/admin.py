from django.contrib import admin
from .models import Group, Message, Event 
# Register your models here.

admin.site.register(Group)
admin.site.register(Message)
admin.site.register(Event)