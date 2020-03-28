from django.db import models


class OperatorTestModel(models.Model):
    operator = models.CharField("Operator type", max_length=32, choices=[])
    value = 5
