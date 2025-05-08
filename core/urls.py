
from django.contrib import admin
from django.urls import path, include
from pacientes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('pacientes.urls'))
]
