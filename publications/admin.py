from django.contrib import admin
from .models import Publications
from django.contrib.admin import register, ModelAdmin
from django.utils.html import format_html

# Register your models here.

admin.site.register(Publications)