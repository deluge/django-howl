from django.db import models
from howl.models import Observer


class Watchdog(models.Model):
    observer = models.ForeignKey(Observer, on_delete=models.PROTECT)
    number = models.PositiveIntegerField()
