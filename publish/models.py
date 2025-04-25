from django.db import models
from django.contrib.auth import get_user_model 


User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField('Title', max_length = 250)
    content = models.TextField('Content')
    slug = models.SlugField('Slug')


    def __str__(self):
        return self.title
