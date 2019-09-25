from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

# Create your views here.

from .models import Rubros
class ListarRubros(ListView):
    model = Rubros
    template_name = 'rubros/listarRubro.html'

class DetalleRubros(DetailView):
    model = Rubros
    template_name = 'rubros/detalleRubro.html'

class CrearRubros(CreateView):
    model = Rubros #Indicamos con el modelo que vamos a trabajar
    template_name = 'rubros/nuevoRubro.html'
    success_url = reverse_lazy('rubros:listarRubro') #success_url sirve para direccionar la vista cuando la operacion es correcta
    fields = '__all__'


    