from django.shortcuts import render
from django.views.generic.list import ListView
from apps.rubros.models import Rubros
from django.contrib.auth.decorators import login_required #Llama a la funcion del decorador para entrar al login

def Inicio(request):
	return render(request,'start.html')

class ListarRubros(ListView):
    model = Rubros
    template_name = 'start.html'