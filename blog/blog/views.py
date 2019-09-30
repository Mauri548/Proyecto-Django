from django.shortcuts import render
from django.views.generic.list import ListView
from apps.rubros.models import Rubros
from apps.productos.models import Producto
from django.contrib.auth.decorators import login_required #Llama a la funcion del decorador para entrar al login

def Inicio(request):
	return render(request,'start.html')

class ListarRubros(ListView):
    model = Rubros
    template_name = 'start.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ListarRubros, self).get_context_data(**kwargs)
    #     context_object_name = 'rub'
    #     list_rubro = Rubros.objects.all()
    #     context['rub'] = list_rubro
    #     return context

# def LisRubro(request):
#     context = {}
#     context['list_rubro'] = Rubros.objects.all()
#     return render(request,'base_template.html',context)
