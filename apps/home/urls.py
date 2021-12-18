from django.contrib import admin
from django.urls import path

# El punto hace referencia a las vistas de la misma carpeta o de la misma aplicación
from . import views

urlpatterns = [
    #Para ejecutar una vista generica en la url hay que utilizar un submétodo que es as_view()
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
]