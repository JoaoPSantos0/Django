from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('teste/', views.pacientes, name="pacientes"),
    path('', views.home, name="home"),
    path('cadastro/', views.register, name="register"),
    path('agendamento/', views.agendar, name="agendar"),
    path('principal/', views.mainRed, name="main"),
    path('agendamentos/', views.agendamentos, name="agendamentos"),
    path('excluir/<int:pk>', views.deletePaciente, name="excluir"),
    path('editar/<int:pk>', views.editPaciente, name="editar"),
]
