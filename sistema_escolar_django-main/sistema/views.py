from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # print('Página inicial funcionou')
    # return HttpResponse('Página inicial')
    return render(
        request,
         'desgraça'
    )

# def cadastro(request):
#     print('Página cadastro funcionou')
#     return HttpResponse('Página inicial do cadastro')