from django.db import models

class Livro(models.Model):
    tombo = models.IntegerField(primary_key=True, unique=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    local_editora = models.CharField(max_length=255)
    ano_edicao = models.CharField(max_length=255)
    data_entrada = models.DateField()
    data_criado = models.DateTimeField(auto_now_add=True)
    data_atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo