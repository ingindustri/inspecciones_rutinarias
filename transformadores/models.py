from django.db import models

# Opciones para el tipo de transformador
TIPO_TRANSFORMADOR = [
    ('TR1', 'MT1 300MVA'),
    ('TR2', 'MT2 300MVA'),
    ('TR3', 'IP T-1 50 MVA'),
]

class InspeccionTransformador(models.Model):
    fecha = models.DateField()
    subestacion = models.CharField(max_length=50)
    tipo_transformador = models.CharField(max_length=4, choices=TIPO_TRANSFORMADOR, default='TR1')  # 👈 Nuevo campo
    temperatura_devanado = models.CharField(max_length=5, default='-')
    temperatura_aceite = models.CharField(max_length=5, default='-')
    nivel_aceite_tanque = models.CharField(max_length=20, default='-')
    nivel_aceite_conmutador = models.CharField(max_length=20, default='-')
    nivel_de_aceite_bushings = models.CharField(max_length=20, default='-')
    estado_funcionamiento_ventiladores= models.CharField(max_length=20, default='-')
    oxido_y_corrosión= models.CharField(max_length=20, default='-')
    pintura= models.CharField(max_length=20, default='-')
    vibracion_ruido= models.CharField(max_length=20, default='-')
    fugas_de_aceite= models.CharField(max_length=20, default='-')
    estado_de_aisladores= models.CharField(max_length=20, default='-')
    limpieza_de_transformadores= models.CharField(max_length=20, default='-')
    limpieza_de_radiadores= models.CharField(max_length=20, default='-')
    control_de_silica_gel= models.CharField(max_length=20, default='-')
    chequeo_de_circuitos_de_control= models.CharField(max_length=20, default='-')
    revisión_de_conexiones_a_tierra= models.CharField(max_length=20, default='-')
    posición_de_taps= models.CharField(max_length=20, default='-')
    indicador_de_cambio_de_tap_en_area_sombreada= models.CharField(max_length=20, default='-')
    numero_de_operaciones_del_cambiador_de_taps= models.CharField(max_length=20, default='-')
    estado_de_pararrayos= models.CharField(max_length=20, default='-')
    contador_de_descarga_de_pararrayos= models.CharField(max_length=20, default='-')
    estado_general = models.CharField(max_length=20)
    observaciones = models.TextField()
