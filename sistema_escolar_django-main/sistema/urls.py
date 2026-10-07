from django.contrib import admin
from django.urls import path,include #erro1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls'))
]

# admin.site.urls