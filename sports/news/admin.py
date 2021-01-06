from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_published', 'category', 'author')
    search_fields = ('title', 'content')


admin.site.register(News, NewsAdmin)
