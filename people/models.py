from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    webpageurl = models.CharField(max_length = 200)
    shortdescription = models.CharField(max_length=200)
    image = models.ImageField(upload_to='professor_portraits/', default='noimage.png')
    def __str__(self):
        return self.name

class CurrentTeam(models.Model):
    occupation_choices = (
        ('Postdoc', 'Postdoc'),
        ('PhD Student', 'PhD Student'),
        ('Masters Student', 'Masters Student'),
        ('Undergraduate', 'Undergraduate'),
        ('Staff', 'Staff'),
    )
    name = models.CharField(max_length= 200)
    description = models.CharField(max_length = 1000)
    webpageurl = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='people_portraits/', default = 'noimage.png')
    occupation = models.CharField(max_length = 25, choices = occupation_choices, default = 'Postdoc')
    def __str__(self):
        return self.name + '_' + self.occupation

class alumni(models.Model):
    occupation_choices = (
        ('Postdoc', 'Postdoc'),
        ('PhD Student', 'PhD Student'),
        ('Masters Student', 'Masters Student'),
        ('Undergraduate', 'Undergraduate'),
        ('Staff', 'Staff'),
    )
    name = models.CharField(max_length=200)
    currentposition = models.CharField(max_length=1000)
    webpageurl = models.CharField(max_length=200)
    occupation = models.CharField(max_length=25, choices=occupation_choices, default='Postdoc')
    major = models.CharField(max_length = 200, default='Computer Science')


    def __str__(self):
        return self.name + '_' + self.occupation

