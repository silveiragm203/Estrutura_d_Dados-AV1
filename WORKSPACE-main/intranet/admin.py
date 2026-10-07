from django.contrib import admin   # importa o módulo admin do Django
from intranet import models        # importa nossos models para registrar


# @admin.register é um decorator: conecta a classe AdminConfig ao model Medico
@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):

    # list_display: define quais colunas aparecem na listagem do admin
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo')
    #               ↑ ID   ↑ Nome  ↑ E-mail  ↑ Telefone  ↑ Especialidade ↑ Ativo?


@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):

    list_display = ('id', 'nome', 'email', 'telefone', 'ativo')


@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):

    # paciente_id e medico_id são ForeignKeys: o admin exibe o __str__ deles
    list_display = ('id', 'paciente_id', 'medico_id', 'status')