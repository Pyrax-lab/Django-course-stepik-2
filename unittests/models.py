from django.db import models

# Create your models here.


class Catalog(models.Model):

    title        = models.CharField(max_length=150)
    ISBN         = models.CharField(max_length=150)
    author       = models.CharField(max_length=200)
    price        = models.SmallIntegerField(default=0)
    availability = models.CharField(max_length=300)

    def __str__(self):
        return self.title