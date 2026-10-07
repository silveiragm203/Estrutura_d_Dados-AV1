from django.contrib import admin
from django.urls import path, include
from sistema import views
urlpatterns = [
    path('admin/',  admin.site.urls),
    path('cadastro/', views.cadastro ),
    path('',include('portal.urls.py')) #cadastro.html
]

# admin.site.urls