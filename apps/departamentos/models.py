from django.db import models

# Create your models here.

class Departamento(models.Model): #Se hereda modelo de los modelos que ya existen en django
    name = models.CharField('Nombre del departamento', max_length=50)#campo de tipo texto, antes del max_length se establece como va a aparecer en el administrador de django 'Nombre'
    short_name = models.CharField('Nombre corto', max_length=20, blank=True)
    anulate = models.BooleanField('Anulado', default=False)#valores booleanos False y True y tiene por defecto el estado de falso

    class Meta:#
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['-name']


    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name


