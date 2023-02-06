from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
# https://django-simple-history.readthedocs.io/en/latest/quick_start.html#install

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

    class Meta:
        verbose_name_plural = "Detalhes do usuário"

    def __str__(self):
        return self.cpf
