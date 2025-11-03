Rotas Principais d
O projeto implementa o CRUD completo para a entidade Livro utilizando as Class-Based Views (CBV) genéricas do Django.

Listar Livros (Read - Lista):

URL: /

Função: Utiliza a ListView para exibir a lista completa de todos os livros cadastrados no sistema.

Criar Novo Livro (Create):

URL: /livro/novo/

Função: Utiliza a CreateView para apresentar e processar o formulário de cadastro de um novo livro.

Detalhe do Livro (Read - Detalhe):

URL: /livro/<int:pk>/

Função: Utiliza a DetailView para exibir todas as informações de um livro específico, identificado pelo seu ID (pk).

Editar Livro (Update):

URL: /livro/<int:pk>/editar/

Função: Utiliza a UpdateView para carregar o formulário com os dados existentes e permitir a alteração do registro.

Excluir Livro (Delete):

URL: /livro/<int:pk>/excluir/

Função: Utiliza a DeleteView para solicitar a confirmação e, em seguida, remover o livro do banco de dados.

Prints:

