from django.contrib import admin
from .models import Blog
from django.db import models
from django.forms import TextInput, Textarea
from django.contrib.admin import register, ModelAdmin
from django.utils.html import format_html

# Register your models here.



class blogadmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 60})},
    }

admin.site.register(Blog, blogadmin)