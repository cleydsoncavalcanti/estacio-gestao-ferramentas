from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
# https://django-simple-history.readthedocs.io/en/latest/quick_start.html#install



class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tool_id = models.ForeignKey(
        'Tool',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_start_at = models.DateTimeField()
    scheduled_end_at = models.DateTimeField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Reservas"

    def __str__(self):
        return self.tool_id
