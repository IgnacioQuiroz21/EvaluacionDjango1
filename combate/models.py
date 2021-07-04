from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class Proveedor(models.Model):
    idProv = models.AutoField(verbose_name='ID', serialize=True, auto_created=True, primary_key=True )
    nombre = models.CharField(max_length=100,verbose_name='Nombre del Proveedor')  
    imagen = models.ImageField(upload_to='images',null=True, blank=True)
    

    def __str__(self):
        return self.nombre

class Parche(models.Model):
    idParche = models.AutoField(verbose_name='ID', serialize=True, auto_created=True, primary_key=True)
    nombre =models.ForeignKey(Proveedor,on_delete=CASCADE,verbose_name='Nombre del Proveedor')   
    fechaParche = models.DateField(verbose_name='Fecha del Parche')
    descParche = models.CharField(max_length=200,verbose_name='Descripcion del Parche')

    def __str__(self):
        return str(self.fechaParche)
        
class Anuncio(models.Model):
    idAnuncio = models.IntegerField(verbose_name='ID',null=False, primary_key=True)
    nombre = models.ForeignKey(Proveedor,on_delete=CASCADE,verbose_name='Nombre Del Proveedor')        
    descAnuncio = models.CharField(max_length=200,verbose_name='Descripcion del Parche')

    def __str__(self):
        return str(self.nombre)