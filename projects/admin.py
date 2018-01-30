from django.contrib import admin
from .models import Projects
from django.db import models
from django.forms import TextInput, Textarea
from django.contrib.admin import register, ModelAdmin
from django.utils.html import format_html

# Register your models here.



class projectadmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 80})},
    }

admin.site.register(Projects, projectadmin)