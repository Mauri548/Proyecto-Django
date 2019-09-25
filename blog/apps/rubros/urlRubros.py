from django.contrib import admin
from django.urls import path
from . import views

app_name = 'rubros'

urlpatterns = [
    path('ListarRubro/',views.ListarRubros.as_view(), name="listarRubro"),

    path('DetalleRubro/<int:pk>', views.DetalleRubros.as_view(), name="detalleRubro"),

    path('CrearRubro/', views.CrearRubros.as_view(), name="crearRubro")   
]
