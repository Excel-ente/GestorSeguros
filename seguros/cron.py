from django.utils import timezone
from django.contrib import admin
from gestion.models import Poliza


def actualizar_polizas_vencidas():
    print("hola")
    polizas_vencidas = Poliza.objects.filter(fecha_vencimiento__lte=timezone.now().date())
    for poliza in polizas_vencidas:
        poliza.estado = 'Vencida'
        print(poliza.fecha_vencimiento)
        poliza.save()