from django.contrib import admin

from .models import Event, Tournament, Sponsor

admin.site.register(Event)
admin.site.register(Tournament)
admin.site.register(Sponsor)
