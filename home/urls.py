# projeto/urls.py
from django.urls import path
from .views import ProdutoDetailView

urlpatterns = [
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
]