from django.contrib import admin
from django.urls import path
from . import views

app_name = 'favoritos'

urlpatterns = [
    path('addfav/',views.AddFavorito, name = 'favorit'),
    path('ListFav/',views.ListFav.as_view(), name = 'listfav'),
    path('eliminar/<int:pk>', views.EliminarFav, name='eliminar'),
]

#path('favorito/', views.Fav, name= 'fav')