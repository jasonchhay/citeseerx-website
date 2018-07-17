from django.db import models
from datetime import datetime


# Create your models here.
'''
class PublicationQuerySet(models.QuerySet):
    @property
    def journals(self):
        print(self.filter(category="Journal"))
        return self.filter(category="Journal")

    @property
    def conference(self):
        return self.filter(category="Conference")
'''
class Publication(models.Model):

    YEAR_CHOICES = []
    for r in range(1975, (datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    CATEGORY_CHOICES = (('Journal','Journal Papers'),('Conference','Conference Papers'))
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    year = models.IntegerField(choices=YEAR_CHOICES, default = datetime.now().year)
    venue = models.CharField(max_length = 200)
    link = models.URLField(max_length = 200, blank=True)
    paperfile = models.FileField(upload_to='paper_files/', blank=True)
    category = models.CharField(max_length=25,choices = CATEGORY_CHOICES, default='Journal')

    objects = PublicationQuerySet.as_manager()

    def __str__(self):
        return self.title + ', ' + str(self.year)

