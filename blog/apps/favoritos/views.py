from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Favorito
from apps.productos.models import Producto

import json


class ListFav(ListView):
    # model = Favorito
    template_name= 'favoritos/listar_favoritos.html'

    def get_queryset(self,*arg,**kwarg):
        return Favorito.objects.filter(user = self.request.user)


class EliminarFav(DetailView):
    model = Favorito
    succes_url = reverse_lazy('favoritos:listfav')

def AddFavorito(request):
    if request.is_ajax():
        try:
            productoo = request.GET.get('id', None)
            producto = Producto.objects.get(pk = productoo)
            Favorito.objects.create(user = request.user, producto = producto)
            return HttpResponse(json.dumps({'status':'si'}),content_type='application/json')
        except Exception as a:
            return HttpResponse(json.dumps({'status':'no'}),content_type='application/json')
    else:
        raise Http404