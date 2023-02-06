from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
# https://django-simple-history.readthedocs.io/en/latest/quick_start.html#install

class Tool(models.Model):
    cod = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    voltage = models.DecimalField(max_digits=10, decimal_places=3)
    part_number = models.CharField(max_length=100)
    size = models.DecimalField(max_digits=10, decimal_places=3)
    unit_size = models.CharField(max_length=30)
    tool_type_id = models.ForeignKey(
        'ToolType',
        on_delete=models.CASCADE,
    )
    material = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Ferramentas"

    def __str__(self):
        return self.cod
