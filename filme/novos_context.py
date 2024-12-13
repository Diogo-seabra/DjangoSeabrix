from .models import Filme, Serie
from itertools import chain


def lista_midias(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    lista_series = Serie.objects.all().order_by('-data_criacao')[0:8]

    # Combine os dois QuerySets
    conteudo = sorted(
        chain(lista_filmes, lista_series),
        key=lambda x: x.data_criacao,
        reverse=True
    )[:14]

    # Define o destaque
    midia_destaque = conteudo[0] if conteudo else None

    # Conteúdo em alta com base em visualizações
    conteudo_em_alta = sorted(
        conteudo,
        key=lambda x: x.visualizacoes,
        reverse=True
    )[:14]

    return {
        "lista_filmes": lista_filmes,
        "lista_series": lista_series,
        "midia_destaque": midia_destaque,
        "conteudo": conteudo,
        "conteudo_em_alta": conteudo_em_alta,
    }


