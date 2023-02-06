from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
# https://django-simple-history.readthedocs.io/en/latest/quick_start.html#install

class Maintenance(models.Model):
    tool_id = models.ForeignKey(
        'Tool',
        on_delete=models.CASCADE,
    )
    TYPES_OF_MAINTENANCE = [
        (1, 'Preventiva'),
        (2, 'Corretiva')
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPES_OF_MAINTENANCE,
        default=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_start_at = models.DateTimeField()
    scheduled_end_at = models.DateTimeField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Manutenções"

    def __str__(self):
        return self.tool_id
