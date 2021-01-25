from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import render
from .models import Autori, Generi, Libri, Editori

# Create your views here.

@login_required
def libreria(request):
    autori = Autori.objects.all()
    editori = Editori.objects.all()
    libri = Libri.objects.all()
    generi = Generi.objects.all()
    context = {'autori': autori, 'editori': editori, 'libri': libri, 'generi': generi}
    return render(request, 'libreria.html', context)


class LibroDetailView(LoginRequiredMixin, DetailView):
    model = Libri
    template_name = 'libro_detail.html'


class LibroListView(LoginRequiredMixin, ListView):
    model = Libri
    template_name = 'lista_libri.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libri'] = Libri.objects.all()
        return context

class EditoriDetailView(LoginRequiredMixin, DetailView):
    model = Editori
    template_name = 'editori_detail.html'

class EditoriListView(LoginRequiredMixin, ListView):
    model = Editori
    template_name = 'lista_editori.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['editori'] = Editori.objects.all()
        return context

class AutoriDetailView(LoginRequiredMixin, DetailView):
    model = Autori
    template_name = 'autore_detail.html'


class AutoriListView(LoginRequiredMixin, ListView):
    model = Autori
    template_name = 'lista_autori.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autori'] = Autori.objects.all()
        return context


class GeneriDetailView(LoginRequiredMixin, DetailView):
    model = Generi
    template_name = 'genere_detail.html'

class GeneriListView(LoginRequiredMixin, ListView):
    model = Generi
    template_name = 'lista_generi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generi'] = Generi.objects.all()
        return context
    