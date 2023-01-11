from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Project, TechStack


@admin.register(Project)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'created_at')
    list_filter = ('created_at',)
    list_display_links = ('id', 'title',)
    list_per_page = 100
    list_max_show_all = 10
    search_fields = ('title',)


@admin.register(TechStack)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')