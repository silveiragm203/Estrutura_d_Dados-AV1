from django import forms

from models import Professor
#erro6
class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
