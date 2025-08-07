from django.db import models

OPCIONES_ESTADO = [
    ('C', 'Correctivo'),
    ('P', 'Preventivo'),
    ('-', 'No requiere mantenimiento'),
]

class InspeccionLinea(models.Model):
    linea_transmision = models.CharField(max_length=20)
    terna = models.CharField(max_length=50,default='-')
    fecha = models.DateField()
    numero_torre = models.CharField(max_length=20, default='-')
    pintura = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default='-')
    estructuras = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default='-')
    fundaciones = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default='-')
    pernos = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default='-')
    conductor = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default='-')
    aisladores = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default='-')
    herrajes = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default='-')
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.linea_transmision} - Torre {self.numero_torre}"

