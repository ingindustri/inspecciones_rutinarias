from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_lineas, name='menu_lineas'),
    path('registrar/', views.registrar_inspeccion_linea, name='registrar_inspeccion_linea'),
    path('registrar_linea/', views.formulario_linea, name='formulario_linea'),
    path('exito_linea/', views.exito_linea, name='registro_exitoso_lineas'),
    path('descargar_excel_lineas/', views.descargar_excel_lineas, name='descargar_excel_lineas'),
    path('limpiar_excel_lineas/', views.limpiar_excel_lineas, name='limpiar_excel_linea'),
]
