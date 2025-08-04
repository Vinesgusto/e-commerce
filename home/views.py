from django.shortcuts import render

# views.py
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import CadastroForm
from django.views import View
from .models import Produto



class HomeView(ListView):
    model = Produto
    template_name = 'home.html'
    context_object_name = 'produtos'

class LoginUsuario(LoginView):
    template_name = 'login.html'

class LogoutUsuario(LogoutView):
    next_page = reverse_lazy('login')

class CadastroUsuario(CreateView):
    template_name = 'cadastro.html'
    form_class = CadastroForm
    success_url = reverse_lazy('login')
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto = self.get_object()
        context['avaliacoes'] = produto.avaliacoes.all()
        return context

class AdicionarAoCarrinhoView(View):
    def post(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        quantidade = int(request.POST.get('quantidade', 1))

        carrinho = request.session.get('carrinho', {})

        if str(produto.id) in carrinho:
            carrinho[str(produto.id)] += quantidade
        else:
            carrinho[str(produto.id)] = quantidade

        request.session['carrinho'] = carrinho
        return redirect('carrinho')
    


def adicionar_ao_carrinho(request, produto_id):
        produto = get_object_or_404(Produto, id=produto_id)
        carrinho = request.session.get('carrinho', {})

        quantidade = int(request.POST.get('quantidade', 1))
        produto_id_str = str(produto.id)

        if produto_id_str in carrinho:
            carrinho[produto_id_str]['quantidade'] += quantidade
        else:
            carrinho[produto_id_str] = {
                'nome': produto.nome,
                'preco': float(produto.preco),
                'quantidade': quantidade
            }

        request.session['carrinho'] = carrinho
        return redirect('carrinho')

def remover_do_carrinho(request, produto_id):
        carrinho = request.session.get('carrinho', {})
        carrinho.pop(str(produto_id), None)
        request.session['carrinho'] = carrinho
        return redirect('carrinho')

def atualizar_quantidade(request, produto_id):
        if request.method == 'POST':
            nova_quantidade = int(request.POST.get('quantidade', 1))
            carrinho = request.session.get('carrinho', {})
            if str(produto_id) in carrinho:
                carrinho[str(produto_id)]['quantidade'] = nova_quantidade
                request.session['carrinho'] = carrinho
        return redirect('carrinho')

    
    
    
class CarrinhoView(View):
    def get(self, request):
        carrinho = request.session.get('carrinho', {})
        produtos = Produto.objects.filter(id__in=carrinho.keys())

        carrinho_itens = []
        total = 0
        for produto in produtos:
            quantidade = carrinho[str(produto.id)]
            subtotal = quantidade * produto.preco
            total += subtotal
            carrinho_itens.append({
                'produto': produto,
                'quantidade': quantidade,
                'subtotal': subtotal
            })

        context = {
            'itens': carrinho_itens,
            'total': total
        }
        return render(request, 'carrinho.html', context)
    
