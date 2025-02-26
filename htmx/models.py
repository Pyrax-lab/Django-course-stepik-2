from django.db import models
from django.utils.translation import gettext_lazy as _lazy
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=150, verbose_name=_lazy('Title'))
    author = models.CharField(max_length=150, verbose_name=_lazy('Author'))
    price = models.PositiveIntegerField(default=0, verbose_name=_lazy('Price'))
    read = models.BooleanField(default=False, verbose_name=_lazy('Read'))

    def __str__(self):
        return self.title