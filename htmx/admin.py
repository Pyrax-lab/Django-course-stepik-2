from django.contrib import admin
from htmx.models import Books 
# Register your models here.

@admin.register(Books)
class AdminBooks(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'read')
    