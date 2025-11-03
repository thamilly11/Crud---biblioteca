# livros/views.py

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Livro
from django.urls import reverse_lazy

# 1. READ (Lista de Livros)
class LivroListView(ListView):
    model = Livro
    template_name = 'livros/listar.html'  # Nome do template: listar.html
    context_object_name = 'livros' # Nome da variável que será passada para o template

# 2. READ (Detalhe de um Livro)
class LivroDetailView(DetailView):
    model = Livro
    template_name = 'livros/detalhe.html' # Nome do template: detalhe.html
    context_object_name = 'livro'

# 3. CREATE (Criar novo Livro)
class LivroCreateView(CreateView):
    model = Livro
    template_name = 'livros/form.html' # Nome do template: form.html
    # Campos que estarão no formulário
    fields = ['titulo', 'autor', 'ano_publicacao', 'isbn', 'genero'] 
    
    # O redirecionamento após o sucesso é definido em get_absolute_url no Model.

# 4. UPDATE (Editar Livro)
class LivroUpdateView(UpdateView):
    model = Livro
    template_name = 'livros/form.html' # Nome do template: form.html (reaproveitado)
    fields = ['titulo', 'autor', 'ano_publicacao', 'isbn', 'genero']

# 5. DELETE (Deletar Livro)
class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'livros/confirm_delete.html' # Nome do template: confirm_delete.html
    context_object_name = 'livro'
    # URL para redirecionar após a exclusão (ListView)
    success_url = reverse_lazy('listar_livros')