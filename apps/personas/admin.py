from typing import List
from django.contrib import admin

from apps.departamentos.models import Departamento

from .models import Empleado, Habilidades

# Register your models here.


admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'job',
        'departamento',
        'Nombre_Completo', #Para colocar algún campo que no esta en el modelo y se define una funcion abajo
    )

    def Nombre_Completo(self, obj):
        print(obj) #Imprime en terminal
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('job', 'habilidades', 'departamento')
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)