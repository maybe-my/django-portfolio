from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Project


@admin.register(Project)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')