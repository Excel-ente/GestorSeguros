from django.contrib import admin
from .models import Poliza,Siniestro
from .actualizador import actualizar_polizas_vencidas

class PolizaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'cobertura', 'bien', 'estado', 'vencimiento_De_poliza')
    exclude = ('fecha_vencimiento', 'estado',)
    actions=[actualizar_polizas_vencidas,]

    def vencimiento_De_poliza(self, obj):
        if obj.fecha_vencimiento:
            formateo = f"📅 {obj.fecha_vencimiento.strftime('%d/%m/%Y')}"
        else:
            formateo = f"-"
        return formateo

admin.site.register(Poliza, PolizaAdmin)
@admin.register(Siniestro)
class PolizaAdmin(admin.ModelAdmin):
    list_display=('Fecha_siniestro','estado','Cliente','Aseguradora_Tercero','Vencimiento',)
    exclude=('cliente','estado',)
    ordering=('fecha_siniestro',)
    

    def Fecha_siniestro(self, obj):
        formateo = f"📅 {obj.fecha_siniestro.strftime('%d/%m/%Y')}"
        return formateo
    
    def Cliente(self, obj):
        formateo = f"👤 {obj.poliza_cliente.cliente}"
        return formateo
    
    def Aseguradora_Tercero(self, obj):
        formateo = f"{obj.compania_tercero.upper()}"
        return formateo

    def Vencimiento(self, obj):
        formateo = f"📅 {obj.vencimiento_siniestro.strftime('%d/%m/%Y')}"
        return formateo