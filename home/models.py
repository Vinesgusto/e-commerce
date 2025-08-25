from django.db import models

# models.py

from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    video = models.FileField(upload_to='produtos/videos/', blank=True, null=True)
    estoque = models.PositiveIntegerField()
    formas_pagamento = models.TextField(help_text="Ex: Pix, Boleto, Cartão em até 3x")

    def __str__(self):
        return self.nome
    
class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='imagens')
    arquivo = models.ImageField(upload_to='produtos/')


class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} avaliou {self.produto.nome}'
