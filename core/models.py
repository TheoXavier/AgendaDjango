from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    dataEvento = models.DateTimeField(verbose_name='Data do evento')
    dataCriacao = models.DateTimeField(auto_now=True, verbose_name='Data da criação')
    local = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.dataEvento.strftime('%d/%m/%Y %H:%M')

    def get_data_input_evento(self):
        return self.dataEvento.strftime('%Y-%m-%dT%H:%M')
