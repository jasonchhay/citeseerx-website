from django.contrib import admin
from .models import Professor, CurrentTeam, alumni
from django.contrib.admin import register, ModelAdmin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.html import format_html

# Register your models here.

admin.site.register(Professor)
admin.site.register(alumni)

class currentteamadmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 60})},
    }

admin.site.register(CurrentTeam, currentteamadmin)