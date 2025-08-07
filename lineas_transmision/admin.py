from django.contrib import admin
from .models import InspeccionLinea

@admin.register(InspeccionLinea)
class InspeccionLineaAdmin(admin.ModelAdmin):
    list_display = ('numero_torre', 'linea_transmision', 'terna', 'fecha')
    search_fields = ('numero_torre', 'linea_transmision', 'terna')
    list_filter = ('linea_transmision', 'terna', 'fecha')

