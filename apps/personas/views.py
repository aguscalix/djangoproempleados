from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

from apps import personas

from .models import Empleado

# Create your views here.


class listar_empleadosListView(ListView):
    model = Empleado
    paginate_by = 5
    template_name = "personas/listar_todos.html"


class listarxareaListView(ListView):
    template_name = "personas/lista_x_area.html"
    

    def get_queryset(self):

        area = self.kwargs['name'] #Para recoger un parametro desde url

        lista = Empleado.objects.filter(
            departamento__name = area
        )

        return lista


class EmpleadosKwordListView(ListView):
    template_name = "personas/por_kword.html"
    context_object_name = 'colaboradores' #Para acceder a la lista

    def get_queryset(self):
        
        palabraClave = self.request.GET.get("kword", '') 

        lista = Empleado.objects.filter(
            first_name = palabraClave
        )

        return lista

class HabilidadesEmpleado(ListView):
    template_name = "personas/habilidades.html"
    context_objects_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado #Obligatorio en DetailView
    template_name = "personas/detalle_empleado.html"

    #Método que sirve para enviar una variable extra hacia el template
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        return context


class SuccessView(TemplateView):
    template_name = "personas/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "personas/add.html"
    fields = ('first_name', 'last_name', 'job', 'departamento', 'habilidades')
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
    
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.savev()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "personas/update.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades',]
    success_url = reverse_lazy('persona_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
    
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "personas/delete.html"
    success_url = reverse_lazy('persona_app:correcto')








