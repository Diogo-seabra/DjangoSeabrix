from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario, Serie
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models


# Create your views here.
class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: #usuario esta autenticado:
            # redireciona para a homefilmes
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs) # redireciona para a homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list -> lista de itens do modelo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona a propriedade conteudo_visto do usuário ao contexto
        context['conteudo_visto'] = self.request.user.conteudo_visto
        return context


class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        # contabilizar uma visualização
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da página (object)
        # self.get_object()
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria).exclude(id=self.get_object().id)[:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context


class Detalhesserie(LoginRequiredMixin, DetailView):
    template_name = "detalhesserie.html"
    model = Serie
    # object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        # contabilizar uma visualização
        serie = self.get_object()
        serie.visualizacoes += 1
        serie.save()
        usuario = request.user
        usuario.series_vistas.add(serie)
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesserie, self).get_context_data(**kwargs)
        # filtrar a minha tabela de series pegando as series cuja categoria é igual a categoria da serie da página (object)
        series_relacionadas = Serie.objects.filter(categoria=self.get_object().categoria).exclude(id=self.get_object().id)[:5]
        context["series_relacionadas"] = series_relacionadas
        return context


class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    context_object_name = 'resultados'  # Nome para usar no template

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        termo_pesquisa = termo_pesquisa.lower()
        if termo_pesquisa:
            filmes = Filme.objects.filter(titulo__icontains=termo_pesquisa).annotate(tipo=models.Value('filme', output_field=models.CharField()))
            series = Serie.objects.filter(titulo__icontains=termo_pesquisa).annotate(tipo=models.Value('serie', output_field=models.CharField()))
            return list(filmes) + list(series)
        else:
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')  # Passa o termo de pesquisa para o template
        return context



class Paginaperfil(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def get_success_url(self):
        return reverse('filme:homefilmes')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')
