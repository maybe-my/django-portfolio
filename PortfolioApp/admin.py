from .models import Project, TechStack
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.utils.html import mark_safe


@admin.register(Project)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'url', 'created_at')
    list_filter = ('created_at',)
    list_display_links = ('id', 'title',)
    list_per_page = 100
    list_max_show_all = 10
    search_fields = ('title',)


@admin.register(TechStack)
class TechStackAdmin(ImportExportModelAdmin):
    list_display = ('title', 'created_at', 'image_img',)
    readonly_fields = ('image_img',)

    def image_img(self, obj):
        if obj.icon_svg:
            return mark_safe(obj.icon_svg)

    image_img.short_description = 'ICON'
