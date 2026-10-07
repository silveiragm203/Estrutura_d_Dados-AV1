from django.contrib import admin
from aluno import models

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','id','telefone','ativo',)
