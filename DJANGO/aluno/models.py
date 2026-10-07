from django.db import models
from django.utils import timezone

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=20)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    matricula = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome}'
