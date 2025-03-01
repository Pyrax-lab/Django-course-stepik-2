from django.db import models

# Create your models here.


class Post(models.Model):
    slug = models.SlugField(max_length=250)
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=1000)

    def __str__(self): return self.title