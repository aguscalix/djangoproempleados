from django.db.models import fields
from django.shortcuts import render

#Paquete de vistas genéricas que tiene django y que trabajan bajo vistas basadas en clase.
from django.views.generic import TemplateView, ListView, CreateView

from .models import Prueba # Se importa la tabla Prueba para usarla en las vistas genericas 

from .forms import PruebaForm

# Create your views here.


#Vistas genéricas

    #Cada vista requiere de sus propios parámetros por ejemplo a un modelo o una consulta a una base de datos

    #TemplateView 
    #ListView
    #CreateView
    #UpdateView

    #Todas solicitan parametros como template_name que es un archivo HTML y que estan alojadas en una carpeta llamada templates

    #QUIEN LLAMA UN TEMPLATE ES UNA VISTA



class PruebaView(TemplateView): #VISTA GENERICA PARA MOSTRAR EXCLUSIVAMENTE UN ARCHIVO HTML
    template_name = 'home/prueba.html' 


class PruebaListView(ListView): #ESTA VISTA SIRVE PARA PROCESOS DE LISTADO QUE VIENE DE LA BASE DE DATOS
    template_name = "home/lista.html" # template a donde se visualizara la lista
    context_object_name = 'listaNumeros' # parámetro que usa ListView para declarar una especie de variable para hacer referencia a los datos de la lista del queryset EN EL ARCHIVO HTML SE LLAMA ESTA VARIABLE DE ESTA FORMA {{listaNumeros}}
    queryset = ['0', '10', '20', '100'] # parametro que sirve para pasar directamente una lista manual si todavia no se esta usando un modelo de base de datos. 

class ListarPruebaListView(ListView): #ESTA VISTA SIRVE PARA PROCESOS DE LISTADO QUE VIENE DE LA BASE DE DATOS
    model = Prueba # Se referencia a la tabla Prueba para listar
    context_object_name = 'lista' # parámetro que usa ListView para declarar una especie de variable para hacer referencia a los datos de la tabla Prueba EN EL ARCHIVO HTML SE LLAMA ESTA VARIABLE DE ESTA FORMA {{lista}}
    template_name = "home/lista-prueba.html" # template a donde se visualizara la lista



class PruebaCreateView(CreateView): # Registra datos a un modelo de base de datos desde un template personalizada
    template_name = "home/add.html" # template a donde se visualizara la lista
    model = Prueba# Se referencia a la tabla Prueba para agregar o crear nuevos datos a la base de datos
    form_class = PruebaForm
    success_url = '/'

    #se le indica a que parametros hay que registrar datos en la tabla o modelo
    fields = ['titulo', 'subtitulo', 'cantidad']


  