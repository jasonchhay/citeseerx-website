from django.contrib import admin
from .models import TeamMember
from django.contrib.admin import register, ModelAdmin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.html import format_html

# Register your models here.

class currentteamadmin(admin.ModelAdmin):
    '''
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 60})},
    }
    '''
    list_display = ['id','fullname', 'image','role', 'category']

admin.site.register(TeamMember, currentteamadmin)
