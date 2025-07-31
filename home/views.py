from django.shortcuts import render

# views.py

from django.views.generic import DetailView
from .models import Produto

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto = self.get_object()
        context['avaliacoes'] = produto.avaliacoes.all()
        return context



