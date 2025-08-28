# projeto/urls.py
from django.urls import path
from .views import ProdutoDetailView
from django.conf.urls.static import static
from django.conf import settings
from home.views import CarrinhoView, AdicionarAoCarrinhoView
from accounts.views import register_view, login_view, logout_view, profile_view

urlpatterns = [
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cadastro/', register_view, name='cadastro'),
    path('carrinho/', CarrinhoView.as_view(), name='carrinho'),
    path('adicionar-ao-carrinho/<int:pk>/', AdicionarAoCarrinhoView.as_view(), name='adicionar_ao_carrinho'),
    path('profile/', profile_view, name='profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)