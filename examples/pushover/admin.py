from django.contrib import admin

from .models import Watchdog


@admin.register(Watchdog)
class WatchdogAdmin(admin.ModelAdmin):
    list_display = ('observer', 'number')
