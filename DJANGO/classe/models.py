from django.db import models
from django.utils import timezone







# Create your models here.
class Classe(models.Model):
    turma = models.CharField(max_length=20)