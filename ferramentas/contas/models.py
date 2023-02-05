from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
# https://django-simple-history.readthedocs.io/en/latest/quick_start.html#install


class ToolType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    time_for_maintenance_in_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()


class Tool(models.Model):
    cod = models.CharField(max_length=30)
    description = models.TextField()
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


class UserDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    work_shift = models.CharField(max_length=30)
    team_id = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()


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
