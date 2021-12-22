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

from .forms import EmpleadoForm

# Create your views here.


class InicioView(TemplateView):
    template_name = "inicio.html"



class listar_empleadosListView(ListView):
    paginate_by = 4 # cuando se aplica este parametro, este listview internamente crea un objeto de paginacion y podra ser enviado al template
    template_name = "personas/listar_todos.html"
    ordering = 'first_name'
    context_object_name = 'empleado' # parámetro que usa ListView para declarar una especie de variable para hacer referencia a los datos de la lista del queryset EN EL ARCHIVO HTML SE LLAMA ESTA VARIABLE DE ESTA FORMA {{empleado}}

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )  
        return lista


class ListaEmpleadosAdminListView(ListView):
    model = Empleado
    template_name = "personas/lista_empleados.html"
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'




class listarxareaListView(ListView):
    template_name = "personas/lista_x_area.html"

    context_object_name = 'empleado'
    

    def get_queryset(self):

        area = self.kwargs['shortname'] #Para recoger un parametro desde url shorname es como una variable y que se coloca en el url

        lista = Empleado.objects.filter( # en esta lista guardamos el filtrado de datos
            departamento__short_name = area #del modelo departamento
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
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:lista_empleado')

    def form_valid(self, form):
    
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "personas/update.html"
    fields = ['first_name', 'last_name', 'full_name' 'job', 'departamento', 'habilidades',]
    success_url = reverse_lazy('persona_app:lista_empleado')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
    
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "personas/delete.html"
    success_url = reverse_lazy('persona_app:lista_empleado')
    








