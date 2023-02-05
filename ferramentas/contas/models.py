from django.db import models


class Categoria(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dt_teste = models.DateTimeField(auto_now_add=True)
