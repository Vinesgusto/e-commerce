from django.contrib import admin
from .models import Produto, Avaliacao
from django.utils.html import format_html

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    search_fields = ('nome',)
    list_filter = ('formas_pagamento',)

    def preview_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="height: 50px;" />', obj.imagem.url)
        return "-"
    preview_imagem.short_description = 'Imagem'

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'usuario', 'nota', 'data')
    search_fields = ('produto__nome', 'usuario__username')
    list_filter = ('nota', 'data')


# Register your models here.
