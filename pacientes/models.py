from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=35)
    email = models.EmailField()
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.name



class Paciente(models.Model):
    nome = models.CharField(max_length=35)
    peso = models.FloatField()
    altura = models.FloatField()
    tipo_sangue = models.CharField(max_length=4)
    sintomas = models.TextField(max_length=200)
    data_agendamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome