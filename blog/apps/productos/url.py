from django.contrib import admin
from django.urls import path
from . import views



app_name = 'productos'

urlpatterns = [
    path('Listar/',views.ListarProductos.as_view(), name="listar"), #

    path('Detalle/<int:pk>', views.DetalleProducto.as_view(), name="detalle"),

    path('Crear/', views.CrearProductos.as_view(), name="crear"),

    # path('ProductoXRubro/<int:pk>', views.ProductoXRubro, name="PxR"),

    path('ListarProducto/<int:pk>', views.ListarProductosPorRubro.as_view(), name="listprod"),

    path('Filtros/', views.Filtros, name="listarfiltro")
]

