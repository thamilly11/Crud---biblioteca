# livros/urls.py (Você teve que criar este arquivo)

from django.urls import path
from .views import (
    LivroListView, 
    LivroDetailView, 
    LivroCreateView, 
    LivroUpdateView, 
    LivroDeleteView
)

urlpatterns = [
    # READ (Lista)
    path('', LivroListView.as_view(), name='listar_livros'), # << Nome listado no base.html
    
    # CREATE
    path('livro/novo/', LivroCreateView.as_view(), name='criar_livro'), # << Nome listado no base.html
    
    # READ (Detalhe)
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='detalhe_livro'), 
    
    # UPDATE
    path('livro/<int:pk>/editar/', LivroUpdateView.as_view(), name='editar_livro'),
    
    # DELETE
    path('livro/<int:pk>/excluir/', LivroDeleteView.as_view(), name='excluir_livro'),
]