from django.utils import timezone  # fornece data/hora com fuso horário correto
from django.db import models       # módulo principal dos models do Django


# ─── TABELA: medico ───────────────────────────────────────────────────────────
class Medico(models.Model):        # herda de Model → vira tabela no banco

    nome        = models.CharField(max_length=30)   # texto curto, até 30 caracteres
    sobrenome   = models.CharField(max_length=30)   # texto curto, até 30 caracteres
    email       = models.EmailField()               # valida formato de e-mail automaticamente
    criacao_data= models.DateTimeField(             # data/hora de quando o registro foi criado
                      default=timezone.now)         # valor padrão = momento atual
    telefone    = models.CharField(max_length=15)   # string (pode ter traços e parênteses)
    crm         = models.CharField(max_length=6)    # código de registro médico (até 6 dígitos)
    especialidade = models.CharField(max_length=20) # ex: ORTOPEDIA, CARDIOLOGIA
    ativo       = models.BooleanField(default=True) # True/False — se o médico está ativo
    mensagem    = models.TextField(blank=True)      # texto longo, opcional (blank=True)
    imagem      = models.ImageField(                # campo de upload de imagem
                      upload_to='img/%Y/%m',        # salva em media/img/ANO/MES/
                      blank=True)                   # opcional: médico pode não ter foto

    def __str__(self):             # define como o objeto aparece no admin e no terminal
        return f'{self.nome} {self.sobrenome}'  # ex: "João Silva"


# ─── TABELA: paciente ─────────────────────────────────────────────────────────
class Paciente(models.Model):

    nome         = models.CharField(max_length=50)
    sobrenome    = models.CharField(max_length=50)
    email        = models.EmailField()
    telefone     = models.CharField(max_length=15)
    cpf          = models.CharField(max_length=11)  # 11 dígitos sem formatação
    criacao_data = models.DateTimeField(default=timezone.now)
    mensagem     = models.TextField(blank=True)
    ativo        = models.BooleanField(default=True)
    imagem       = models.ImageField(upload_to='img/%Y/%m', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


# ─── TABELA: consulta ─────────────────────────────────────────────────────────
class Consulta(models.Model):

    # ForeignKey cria um relacionamento "muitos para um" (N:1)
    # on_delete=CASCADE: se o paciente for deletado, a consulta também é deletada
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico_id   = models.ForeignKey(Medico,   on_delete=models.CASCADE)

    horario     = models.DateTimeField(default=timezone.now)   # data/hora da consulta
    observacao  = models.TextField(blank=True)                 # anotação opcional

    # choices: lista de opções válidas para o campo
    # formato: lista de tuplas (valor_no_banco, texto_exibido)
    status = models.CharField(
        default='A',    # valor padrão ao criar a consulta
        max_length=1,   # salva apenas 1 caractere no banco (A, X, C ou R)
        choices=(
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada'),
        )
    )

    def __str__(self):
        return f'Consulta {self.get_status_display()} — {self.paciente_id}'
        # get_status_display() retorna o texto legível (ex: "Agendada"), não o código ("A")