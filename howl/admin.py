from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Alert, Observer


@admin.register(Observer)
class ObserverAdmin(admin.ModelAdmin):
    list_display = ('name', 'operator', 'value')


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('get_observer_name', 'timestamp', 'state')
    list_filter = ('state',)

    def get_observer_name(self, obj):
        return obj.observer.name

    get_observer_name.short_description = _('Observer')
