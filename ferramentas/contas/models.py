from django.db import models
from django.contrib.auth.models import User


class TipoFerramenta(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Ferramenta(models.Model):
    codigo = models.CharField(max_length=30)
    descricao = models.TextField()
    voltagem = models.DecimalField()
    part_number = models.CharField(max_length=100)
    tamanho = models.DecimalField()
    unidade = models.CharField(max_length=30)
    tipo_id = models.ForeignKey(
        'TipoFerramenta',
        on_delete=models.CASCADE,
    )
    material = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Cadastro(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    turno = models.CharField(max_length=30)
    equipe_id = models.ForeignKey(
        'Equipe',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Reservas(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ferramenta_id = models.ForeignKey(
        'Ferramenta',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    dt_prevista_inicio = models.DateTimeField()
    dt_prevista_termino = models.DateTimeField()
    dt_inicio = models.DateTimeField()
    dt_termino = models.DateTimeField()


class Manutencao(models.Model):
    ferramenta_id = models.ForeignKey(
        'Ferramenta',
        on_delete=models.CASCADE,
    )
    TIPOS_MANUTENCAO = [
        (1, 'Preventiva'),
        (2, 'Corretiva')
    ]
    tipo = models.CharField(
        max_length=2,
        choices=TIPOS_MANUTENCAO,
        default=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    dt_prevista_inicio = models.DateTimeField()
    dt_prevista_termino = models.DateTimeField()
    dt_inicio = models.DateTimeField()
    dt_termino = models.DateTimeField()
