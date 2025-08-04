# projeto/urls.py
from django.urls import path
from .views import ProdutoDetailView
from home.views import LoginUsuario, LogoutUsuario, CadastroUsuario
from home.views import CarrinhoView, AdicionarAoCarrinhoView

urlpatterns = [
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutUsuario.as_view(), name='logout'),
    path('cadastro/', CadastroUsuario.as_view(), name='cadastro'),
    path('carrinho/', CarrinhoView.as_view(), name='carrinho'),
    path('adicionar-ao-carrinho/<int:pk>/', AdicionarAoCarrinhoView.as_view(), name='adicionar_ao_carrinho'),
]