from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class ToolType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    time_for_maintenance_in_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipos de ferramenta"

    def __str__(self):
        return self.name
