from django.db import models

# Create your models here.

class TeamMember(models.Model):

    category_choices = (
        ('Core Team', 'Core Team'),
        ('Noted Contributors', 'Noted Contributors'),
        ('Founders', 'Founders'),
    )

    fullname = models.CharField(max_length= 200, blank=True)
    role = models.CharField(max_length= 200)
    description = models.TextField(max_length = 1000)
    webpageurl = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='team_portraits', default = 'noimage.png')
    category = models.CharField(max_length = 25, choices = category_choices, default = 'Noted Contributors')




