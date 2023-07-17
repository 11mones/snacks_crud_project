from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy, reverse

class SnacksListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = "data"

class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack

class SnackCreate (CreateView):
    template_name = 'create.html'
    model = Snack
    fields=['name','Autpurchaser','desc']

class SnackUpdate (UpdateView):
    template_name = 'update.html'
    model = Snack
    fields=['name','Autpurchaser','desc']
    success_url = reverse_lazy('snacks')

class SnackDelete (DeleteView):
    template_name = 'delete.html'
    model = Snack
    success_url = reverse_lazy('snacks')
# Create your views here.
