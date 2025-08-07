from django.db import models

OPCIONES_ESTADO = [
    ('C', 'Correctivo'),
    ('P', 'Preventivo'),
    ('-', 'No requiere mantenimiento'),
]

class InspeccionLinea(models.Model):
    linea_transmision = models.CharField(max_length=100)
    terna = models.CharField(max_length=50,default='OK')
    fecha = models.DateField()
    numero_torre = models.CharField(max_length=20, default='OK')
    pintura = models.CharField(max_length=1, choices=OPCIONES_ESTADO, default='OK')
    estructuras = models.CharField(max_length=1, choices=OPCIONES_ESTADO, default='OK')
    fundaciones = models.CharField(max_length=1, choices=OPCIONES_ESTADO, default='OK')
    pernos = models.CharField(max_length=1, choices=OPCIONES_ESTADO, default='OK')
    conductor = models.CharField(max_length=1, choices=OPCIONES_ESTADO, default='OK')
    aisladores = models.CharField(max_length=1, choices=OPCIONES_ESTADO, default='OK')
    herrajes = models.CharField(max_length=1, choices=OPCIONES_ESTADO, default='OK')
    observaciones = models.TextField(blank=True)
    estructuras = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.linea_transmision} - Torre {self.numero_torre}"

