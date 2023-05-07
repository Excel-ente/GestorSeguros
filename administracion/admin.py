from django.contrib import admin
from .models import *

# Register your models here.

#Estos modelos los uso yo, asi que no hace falta la forma de tabla.
admin.site.register(Formadepago)
admin.site.register(Rama)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('documento','nombres','correo_electronico','telefono','polizas_activas',)
    list_display_links=('documento','nombres',)
    exclude=('notificaciones','polizas_activas',)

    def documento(self, obj): 
        formateo = f"{obj.dni}"
        return formateo

    def nombres(self, obj): 
        formateo = f"👤{obj.nombre}, {obj.apellido}"
        return formateo
    
    def correo_electronico(self, obj): 
        formateo = f"📧 {obj.email}"
        return formateo
    
    def telefono(self, obj): 
        formateo = f"📞{obj.contacto}"
        return formateo

    def Tipo_de_pago(self,obj):
        if obj.formaPago.nombre == "EFECTIVO":
            formateo=f"💵 Efectivo"
        elif obj.formaPago.nombre == "TRASNFERENCIA":
            formateo=f"🏦 Trasnferencia"
        elif obj.formaPago.nombre == "MERCADO PAGO":
            formateo=f"🌐 Mercado Pago"  
        elif obj.formaPago.nombre == "TARJETA":
            formateo=f"💳 Tarjeta"  
        else:
            formateo=f"✍️ {obj.formaPago}"  
        return formateo

@admin.register(Bien)
class BienAdmin(admin.ModelAdmin):
    exclude=('fecha_de_vencimiento','estado',)
    list_display=('titular','rama','Bien_Asegurado','estado_De_poliza','vencimiento_De_poliza')
    list_display_links=('rama','titular',)
    exclude=('fecha_de_vencimiento','estado',)

    def vencimiento_De_poliza(self, obj):
        if obj.fecha_de_vencimiento:
            formateo = f"📅 {obj.fecha_de_vencimiento}"
        else:
            formateo = f"-"
        return formateo

    def Bien_Asegurado(self, obj): 

        if obj.rama.nombre=="AUTO":
            formateo = f"🚙 {obj.marca.upper()} {obj.modelo.upper()} {obj.ano}"
        elif obj.rama.nombre=="CAMIONETA":
            formateo = f"🛻 {obj.marca.upper()} {obj.modelo.upper()} {obj.ano}"
        elif obj.rama.nombre=="BICICLETA":
            formateo = f"🚲 {obj.marca.upper()} {obj.modelo.upper()} {obj.ano}"
        elif obj.rama.nombre=="HOGAR":
            formateo = f"🏠 {obj.marca.upper()} {obj.modelo.upper()} {obj.ano}"
        elif obj.rama.nombre=="SEGURO DE VIDA":
            formateo = f"🧗 {obj.marca.upper()} {obj.modelo.upper()} {obj.ano}"
        else:
            formateo = f"{obj.marca.upper()} {obj.modelo.upper()} {obj.ano}"

        return formateo
        
    def estado_De_poliza(self, obj): 
        if obj.estado==True:
            formateo=f"🟢 Vigente | Vence el : {obj.fecha_de_vencimiento}"
        else:
            formateo=f"🔴 Sin Póliza"
        return formateo


class CoberturaAdmin(admin.ModelAdmin):
    list_display=('compania','Categoria','Tipo','plazo_en_dias',)

    def Categoria(self,obj):
        return obj.nombre

    def Tipo(self,obj):

        if obj.rama.nombre=="AUTO":
            formateo=f"🚙 | {obj.rama.nombre} "
        elif obj.rama.nombre=="CAMIONETA":
            formateo=f"🛻 | {obj.rama.nombre} "  
        elif obj.rama.nombre=="HOGAR":
            formateo=f"🏠 | {obj.rama.nombre} "  
        elif obj.rama.nombre=="BICICLETA":
            formateo=f"🚲 | {obj.rama.nombre} "   
        elif obj.rama.nombre=="SEGURO DE VIDA":
            formateo=f"🧗 | {obj.rama.nombre} "
        elif obj.rama.nombre=="OTRO":
            formateo=f"{obj.rama.nombre} "


        return formateo


admin.site.register(Cobertura, CoberturaAdmin)