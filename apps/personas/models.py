from django.db import models

from apps.departamentos.models import Departamento

from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidades'
        verbose_name_plural = 'Habilidades de empleados'

    def __str__(self) -> str:
        return self.habilidad

class Empleado(models.Model):
    job_choices = (
        ('0','TÉCNICO'),
        ('1','DIRECCIÓN'),
        ('2','ASISTENTE DE DIRECCIÓN'),
        ('3','ASISTENTE CONTABLE'),
        ('4','COORDINACIÓN ACADÉMICA'),
        ('5','BIBLIOTECA'),
        ('6','SERVICIO'),
        ('7','CONTADOR GENERAL'),
        ('8','JEFE'),
        ('9','JEFA'),
    )

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField ('Nombre completo', max_length=120, blank=True)
    job = models.CharField('Puesto de trabajo', max_length=1, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name

