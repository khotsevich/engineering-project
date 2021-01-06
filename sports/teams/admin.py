from django.contrib import admin

from .models import Type, Team, Player


class TypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'number')
    search_fields = ('surname', 'name', 'number')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name',)
    list_filter = ('type',)


admin.site.register(Type, TypeAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
