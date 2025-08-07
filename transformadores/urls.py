from django.urls import path
from . import views

urlpatterns = [
    path('menu_transformadores/', views.menu_transformadores, name='menu_transformadores'),
    path('formulario/', views.formulario_transformador, name='form_transformador'),
    path('descargar_excel/', views.descargar_excel, name='descargar_excel'),
    path('limpiar_excel/', views.limpiar_datos_excel, name='limpiar_excel'),  # <-- ESTA LÍNEA
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('inicio/', views.home, name='home'),
]




