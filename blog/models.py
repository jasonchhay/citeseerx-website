from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    date = models.DateField(default = timezone.now)
    blogtitle = models.CharField(max_length = 200)
    postername = models.CharField(max_length = 1000, null=True, blank = True)
    link = models.CharField(max_length = 1000, blank = True)
    description = models.TextField(max_length = 10000)
    def __str__(self):
        return self.blogtitle