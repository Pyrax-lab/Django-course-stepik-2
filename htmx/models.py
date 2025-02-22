from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.PositiveIntegerField(default=0)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title