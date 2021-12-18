from django.db import models

# Create your models here.

""" El ORM de Django es una implementación del concepto de mapeo de objeto relacional (ORM). Una de las características más poderosas de Django es su Mapeador Relacional de Objetos (ORM), que le permite interactuar con su base de datos, como lo haría con instrucciones SQL (Structured Query Language). """

# SI SE CAMBIA DE GESTOR DE BASE DE DATOS LA ORM SE ENCARGA DE VOLVER A MIGRAR ESOS MODELOS 

class Prueba(models.Model): #Tabla Prueba

    #atributos o campos de la tabla
    titulo = models.CharField(max_length=100) #campo tipo texto con longitud maxima 100
    subtitulo = models.CharField(max_length=50)#campo tipo texto con longitud maxima 50
    cantidad = models.IntegerField()#campo tipo entero

    def __str__(self): #Funcion para retornar un dato o varios datos del modelo. 
        return self.titulo + ' ' + self.subtitulo