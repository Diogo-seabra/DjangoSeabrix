from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

LISTA_CATEGORIAS = (
    ("ACAO", "Ação"),
    ("TERROR", "Terror"),
    ("ANIME", "Anime"),
    ("OUTROS", "Outros"),
)


# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    link = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.titulo


# criar os episodios
class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    serie = models.ForeignKey("Serie", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.serie.titulo + " - " + self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")
    series_vistas = models.ManyToManyField("Serie")

    @property
    def conteudo_visto(self):
        return list(self.filmes_vistos.all()) + list(self.series_vistas.all())[::-1]



