from django.db import models
from django.forms import ValidationError


class Formadepago(models.Model):
    nombre=models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.nombre.upper()

class Cliente(models.Model):
    dni=models.CharField(max_length=255,blank=False,null=False)
    nombre=models.CharField(max_length=255,blank=False,null=False)
    apellido=models.CharField(max_length=255,blank=False,null=False)
    direccion=models.CharField(max_length=255,blank=False,null=False)
    fechaNacimiento=models.DateField(blank=False,null=False)
    email=models.EmailField(max_length=255,blank=True,null=True)
    contacto=models.IntegerField(blank=True,null=True)
    polizas_activas=models.IntegerField(default=0,blank=True,null=True)
    formaPago=models.ForeignKey(Formadepago,on_delete=models.PROTECT,default=1,blank=False,null=False)
    datoPago=models.CharField(max_length=255,blank=False,null=False)
    notificaciones=models.BooleanField(default=False)
    comentarios=models.TextField(blank=True,null=True)

    def __str__(self):
        mensaje = f"{self.nombre}, {self.apellido} "
        return f"{self.nombre.upper()}, {self.apellido.upper()}"
    
class Compania(models.Model):
    nombre=models.CharField(max_length=255,blank=False,null=False)
    email=models.EmailField(max_length=255,blank=True,null=True)
    contacto=models.IntegerField(blank=True,null=True)
    comentarios=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.nombre.upper()
    

class Rama(models.Model):
    nombre=models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.nombre.upper()
    

class Cobertura(models.Model):
    nombre=models.CharField(max_length=255,blank=False,null=False)
    compania=models.ForeignKey(Compania,on_delete=models.PROTECT,blank=False,null=False)
    rama=models.ForeignKey(Rama,on_delete=models.PROTECT,default=1  ,blank=False,null=False)
    plazo_en_dias=models.IntegerField(default=30,blank=False,null=False)
    comentarios=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.compania} | {self.nombre} - Plazo: {self.plazo_en_dias} Dias"
    


class Bien(models.Model):
    rama=models.ForeignKey(Rama,on_delete=models.PROTECT,blank=False,null=False)
    titular=models.ForeignKey(Cliente,on_delete=models.PROTECT,blank=False,null=False)
    marca=models.CharField(max_length=255,blank=False,null=False)
    modelo=models.CharField(max_length=255,blank=False,null=False)
    chasis=models.CharField(max_length=255,blank=True,null=True)
    motor=models.CharField(max_length=255,blank=True,null=True)
    ano=models.IntegerField(default=2023,blank=False,null=False)
    estado=models.BooleanField(default=False)
    fecha_de_vencimiento=models.DateField(blank=True,null=True)
    comentarios=models.TextField(blank=True,null=True)

    def __str__(self):

        if self.rama.nombre=="AUTO":
            formateo=f"🚙 {self.marca.upper()} {self.modelo.upper()} {self.ano}"
        elif self.rama.nombre=="CAMIONETA":
            formateo=f"🛻 {self.marca.upper()} {self.modelo.upper()} {self.ano}"
        elif self.rama.nombre=="HOGAR":
            formateo=f"🏠 {self.marca.upper()} {self.modelo.upper()} {self.ano}"
        elif self.rama.nombre=="BICICLETA":
            formateo=f"🚲 {self.marca.upper()} {self.modelo.upper()} {self.ano}" 
        elif self.rama.nombre=="SEGURO DE VIDA":
            formateo=f"🧗 {self.marca.upper()} {self.modelo.upper()} {self.ano}"
        elif self.rama.nombre=="OTRO":
            formateo=f"{self.marca.upper()} {self.modelo.upper()} {self.ano}"
        else:
            pass

        return formateo


    class Meta:
        verbose_name = 'Bien'
        verbose_name_plural ='Bienes' 