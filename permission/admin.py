from django.contrib import admin
from permission.models import Post 
from guardian.admin import GuardedModelAdmin
# Register your models here.

class PostAdmin(GuardedModelAdmin):
    list_display = ('title', )

admin.site.register(Post, PostAdmin)