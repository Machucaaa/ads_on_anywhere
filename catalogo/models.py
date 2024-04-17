from django.db import models
from usuarios.models import Propietario
from shortuuidfield import ShortUUIDField
import datetime
import os

from django.conf import settings

# Create your models here.

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/', filename)


class Categoria(models.Model):
    Id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50,blank=False, null=False)
    esta_activa = models.BooleanField(default=True)    
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    trending = models.BooleanField(default=False, null=True, help_text="0=default , 1=trending")
    created_at = created_at = models.DateTimeField(auto_now_add=True)
    slug = ShortUUIDField(unique=True)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    Id_producto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    precio_original = models.FloatField(default=0.00, null=True)
    precio = models.FloatField(default=0.00)
    existencia = models.FloatField(default=0.00)
    esta_activo = models.BooleanField(default=True, help_text="0=Inactivo , 1=Activo")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    en_oferta = models.BooleanField(default=False, null=True, help_text="0=no oferta , 1=oferta")    
    created_at = models.DateTimeField(auto_now_add=True)
    slug = ShortUUIDField(unique=True)
    cod_barras = models.CharField(max_length=20, blank=True, null=True, default='')

    def __str__(self):
        return self.producto+" "+self.propietario.username
