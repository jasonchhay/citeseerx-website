from django.db import models
from datetime import datetime


# Create your models here.
class Projects(models.Model):
    YEAR_CHOICES = []
    for r in range(1975, (datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))
    projecttitle = models.CharField(max_length = 200)
    people = models.CharField(max_length = 1000, null=True, blank = True)
    year = models.IntegerField(choices=YEAR_CHOICES, default = datetime.now().year)

    link = models.CharField(max_length = 1000, blank = True)
    description = models.TextField(max_length = 10000)
    def __str__(self):
        return self.projecttitle