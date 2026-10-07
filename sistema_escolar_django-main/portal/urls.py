from django.urls import path

from portal import views
#erro8 erro de caminho do sistema
urlpatterns = [
    path('index/', views.index),
    path('cadastro/', views.cadastro),
]
