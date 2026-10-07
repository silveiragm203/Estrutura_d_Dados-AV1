from django.db import models # ORM do Django para declarar modelos no banco de dados.
from django.utils import timezone # Útil para gerar data/hota atual no projeto.

# Modelo que representa um Paciente.
# atributos => nome, sobrenome, email, telefone, data de cadastro, mensagem, ativo(True/False).
class Paciente(models.Model):
    nome = models.CharField(max_length=25) # Nome do paciente.
    sobrenome = models.CharField(max_length=50) # Sobrenome do paciente.
    email = models.EmailField() # Email de contato do paciente.
    telefone = models.CharField(max_length=20) # Telefone de contato.
    criacao_data = models.DateTimeField(default=timezone.now) # Data/hora do cadastro
    mensagem = models.TextField(blank=True) # Campo opcional livre para mensagem.
    ativo = models.BooleanField(default=True) # Campo de exclusão lógica
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

# Modelo que representa um Médico.
class Medico(models.Model):
    nome = models.CharField(max_length=25) # Nome do médico.
    sobrenome = models.CharField(max_length=50) # Sobrenome do médico.
    email = models.EmailField() # Email de contato do médico.
    criacao_data = models.DateTimeField(default=timezone.now) # Data/hora do cadastro
    telefone = models.CharField(max_length=20) # Telefone de contato.
    crm = models.CharField(max_length=6) # CRM do médico.
    especialidade = models.CharField(max_length=50) # Especialidade do médico.
    mensagem = models.TextField(blank=True) # Campo opcional livre para mensagem.
    ativo = models.BooleanField(default=True) # Campo de exclusão lógica
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
# Modelo que representa uma consulta 
# id, id do paciente, id do medico, horario/data, obs, status
class Consulta(models.Model):
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE) # Chave estrangeira
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE) # Chave estrangeira
    data_consulta = models.DateTimeField(default=timezone.now) #Data/hota da consulta
    ativa = models.BooleanField(default=True) # Campo de exclusão lógica
    observacao = models.TextField(blank=True) # Anotação opcional
    status = models.CharField(
        default='A',
        max_length=1,
        choices=[
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada'),
        ]
    )