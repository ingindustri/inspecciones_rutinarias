from django.shortcuts import render, redirect
from .forms import InspeccionLineaForm
from .models import InspeccionLinea
import openpyxl
import os
from django.conf import settings
from django.http import HttpResponse
from django.http import FileResponse

def menu_lineas(request):
    return render(request, 'lineas_transmision/menu_lineas.html')

def registrar_inspeccion_linea(request):
    if request.method == 'POST':
        form = InspeccionLineaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = InspeccionLineaForm()
    return render(request, 'lineas_transmision/formulario_linea.html', {'form': form})

def formulario_linea(request):
    if request.method == 'POST':
        form = InspeccionLineaForm(request.POST)
        if form.is_valid():
            inspeccion = form.save()

            ruta_excel = os.path.join(settings.BASE_DIR, 'registro_lineas.xlsx')
            if os.path.exists(ruta_excel):
                wb = openpyxl.load_workbook(ruta_excel)
                ws = wb.active
            else:
                wb = openpyxl.Workbook()
                ws = wb.active
                ws.append([
                    'Fecha', 'Línea', 'Terna', 'N° Torre', 'Pintura',
                    'Estructuras', 'Fundaciones', 'Pernos',
                    'Conductor', 'Aisladores', 'Herrajes', 'Observaciones'
                ])
            
            ws.append([
                inspeccion.fecha, inspeccion.linea_transmision, inspeccion.terna,
                inspeccion.numero_torre, inspeccion.pintura,
                inspeccion.estructuras, inspeccion.fundaciones,
                inspeccion.pernos, inspeccion.conductor, inspeccion.aisladores,
                inspeccion.herrajes, inspeccion.observaciones
            ])
            wb.save(ruta_excel)
            return redirect('registro_exitoso_lineas')
    else:
        form = InspeccionLineaForm()

    return render(request, 'lineas_transmision/formulario_linea.html', {'form': form})

def descargar_excel_lineas(request):
    ruta_excel = os.path.join(settings.BASE_DIR, 'registro_lineas.xlsx')
    if os.path.exists(ruta_excel):
        return FileResponse(open(ruta_excel, 'rb'), as_attachment=True, filename='registro_lineas.xlsx')
    else:
        return HttpResponse("El archivo no existe aún.", status=404)

def exito_linea(request):
    return render(request, 'lineas_transmision/exito.html')

def limpiar_excel_lineas(request):
    ruta_excel = os.path.join(settings.BASE_DIR, 'registro_lineas.xlsx')
    if os.path.exists(ruta_excel):
        os.remove(ruta_excel)
        return HttpResponse("Archivo Excel de líneas eliminado.")
    else:
        return HttpResponse("El archivo no existe.", status=404)
