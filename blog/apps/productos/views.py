from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import Producto
from apps.rubros.models import Rubros

class ListarProductos(ListView):
    model = Producto
    template_name = 'productos/listar.html'

    def get_context_data(self, **kwargs):
        context = super(ListarProductos, self).get_context_data(**kwargs)
        context_object_name = 'rub'
        list_rubro = Rubros.objects.all()
        context['rub'] = list_rubro
        return context
    

class DetalleProducto(DetailView):
    model = Producto
    template_name = 'productos/detalleProducto.html'

class CrearProductos(CreateView):
    model = Producto #Indicamos con el modelo que vamos a trabajar
    template_name = 'productos/nuevo.html'
    success_url = reverse_lazy('productos:listar') #success_url sirve para direccionar la vista cuando la operacion es correcta
    fields = '__all__' # Se indican los campos que son necesarios, en este caso todos los campos.

# def ProductoXRubro(request, pk):
#     context = {}
#     #if pk == 0:
#     #    p = Producto.objects.all()
#     #else:
#         #r = Rubro.object.get(pk = pk)
#         #p = r.ProductosXRubros.all()
#     # context['list_rubro'] = p
#     # return render(request,'productos/listar.html',context)
#     context['list_rubro'] = Producto.objects.filter(rubro = pk) #object_list es una variable, esta puede tener cualquier nombre
#     return render(request,'productos/listar.html',context)


def Filtros(request):
    context = {}
    rubro = request.GET.get('filtro', None)
    desde = request.GET.get('desde',None)
    hasta = request.GET.get('hasta',None)
    if not desde:
        desde = 0
    if not hasta:
        hasta = 9999999999


    if rubro and rubro != "0":
        context['object_list'] = Producto.objects.filter(rubro = rubro, precio__gte=desde,precio__lte=hasta)
    else:
        context['object_list'] = Producto.objects.filter(precio__gte=desde,precio__lte=hasta)
    context['rubros'] = Rubros.objects.all()
    print(context['rubros'])
    return render(request,'productos/filtro.html',context)

    


class ListarProductosPorRubro(ListView):
    template_name = 'productos/listar.html'
    def get_queryset(self):
        if self.kwargs['pk'] == 0:
            x = Producto.objects.all()
        else:
            x = Producto.objects.filter(rubro=self.kwargs['pk'])
        return x
    
    def get_context_data(self, **kwargs):
        context = super(ListarProductosPorRubro, self).get_context_data(**kwargs)
        context_object_name = 'rub'
        list_rubro = Rubros.objects.all()
        context['rub'] = list_rubro
        return context