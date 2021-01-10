from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import News


def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)


make_published.short_description = "Опубликовать несколько"


class NewsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_published', 'category', 'author')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'is_published', 'category', 'author')
    actions = [make_published]


admin.site.register(News, NewsAdmin)
