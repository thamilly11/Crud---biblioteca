# livros/models.py

from django.db import models
from django.urls import reverse # Importe para usar em get_absolute_url

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    genero = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['titulo']
        verbose_name_plural = "Livros"

    def __str__(self):
        return f"{self.titulo} ({self.autor})"

    def get_absolute_url(self):
        """Define para onde redirecionar após a criação/atualização de um livro."""
        # Redireciona para a página de detalhes após salvar
        return reverse('detalhe_livro', kwargs={'pk': self.pk})