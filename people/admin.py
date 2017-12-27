from django.contrib import admin
from .models import Professor, CurrentTeam, alumni
from django.contrib.admin import register, ModelAdmin
from django.utils.html import format_html

# Register your models here.

admin.site.register(Professor)
admin.site.register(CurrentTeam)
admin.site.register(alumni)

