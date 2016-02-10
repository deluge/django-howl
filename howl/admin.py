from django.contrib import admin

from .models import Alert, Observer


@admin.register(Observer)
class ObserverAdmin(admin.ModelAdmin):
    list_display = ('name', 'operator', 'value')


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'timestamp', 'value', 'state')
    list_filter = ('state',)
