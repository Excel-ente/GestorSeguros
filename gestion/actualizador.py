from django.utils import timezone
from django.contrib import admin
from .models import Poliza

@admin.action(description="Actualizar Polizas")
def actualizar_polizas_vencidas(modeladmin, request, queryset):
   

    polizas = Poliza.objects.all()

    for poliza in polizas:

        #me falta filtrar las fechas

        #if poliza.fecha_vencimiento < timezone.now().date():
        poliza.estado = 'Vencida'
        poliza.save()

