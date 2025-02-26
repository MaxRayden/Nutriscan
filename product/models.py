from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255, blank=True, null=True)
    codigo_de_barras = models.CharField(max_length=50, unique=True)
    ingredientes = models.ManyToManyField('Ingrediente', related_name='produtos')
    restricoes = models.ManyToManyField('RestricaoAlimentar', related_name='produtos', blank=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class RestricaoAlimentar(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)
    ingredientes_perigosos = models.ManyToManyField(Ingrediente, related_name='restricoes')

    def __str__(self):
        return self.nome

class HistoricoConsulta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_consulta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} consultou {self.produto} em {self.data_consulta}"
