from django.shortcuts import render

from django.views.generic import ListView

from django.views.generic.edit import FormView

from .forms import NewDepartamentoForm

from apps.personas.models import Empleado
from .models import Departamento

# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamentos/lista.html"
    context_object_name = 'departamentos'



class NuevoDepartamentoView(FormView):
    template_name = 'departamentos/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['nombreCorto']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']

        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        return super(NuevoDepartamentoView, self).form_valid(form)