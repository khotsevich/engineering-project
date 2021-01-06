from django.contrib import admin

from .models import Event, Tournament, Sponsor


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'status', 'category', 'tournament')
    list_filter = ('time', 'status', 'category', 'tournament')


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'prize_fund', 'sponsor')
    list_filter = ('sponsor',)
    list_editable = ('sponsor',)


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Event, EventAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Sponsor, SponsorAdmin)
