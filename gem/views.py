from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from gem.models import GrupoEstudiantil, Evento, Asistencia, Usuario
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from datetime import datetime



class IndexView(generic.ListView):
    template_name = 'gem/index.html'
    context_object_name = 'eventos_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            # 'eventos_list': Evento.objects.all().order_by('-event_date'),
            'grupos_estudiantiles_list': GrupoEstudiantil.objects.all(),
        })
        return context

    def get_queryset(self):
        return Evento.objects.all().order_by('-event_date')

class DetailView(generic.DetailView):
    model = Evento
    template_name = 'gem/detail.html'
