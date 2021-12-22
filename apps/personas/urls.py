from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar-empleados/', views.listar_empleadosListView.as_view(), name='empleados_all'),
    path('listar-por-area/<shortname>/', views.listarxareaListView.as_view(), name='empleados_area'),
    path('buscar-empleado/', views.EmpleadosKwordListView.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='ver_empleado'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='agregar_empleado'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
    path('lista-empleado-admin/', views.ListaEmpleadosAdminListView.as_view(), name='lista_empleado'),
]
