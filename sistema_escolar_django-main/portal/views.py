from django.shortcuts import render
#erro5 import HTTTP
from django.http import HttpResponse


def index(request):
    # return HttpResponse('Página inicial')
    return render(
        request,
        'templates/portal/index.html',
        )

def cadastro(request):
    return HttpResponse('Página inicial do cadastro')
