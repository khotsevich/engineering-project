from django.contrib import admin

from .models import Podcast


class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'category', 'author')
    list_filter = ('created_at', 'is_published', 'category', 'author')


admin.site.register(Podcast, PodcastAdmin)
