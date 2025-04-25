from django.contrib import admin

# Register your models here.
from .models import User1

@admin.register(User1)
class UserAdmin(admin.ModelAdmin):
    pass
