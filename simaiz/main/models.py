from django.db import models
from django.contrib.auth.models import User
from .choices import *

# Create your models here.

class Planta(models.Model):
    nombre_planta = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    dias_ciclo = models.IntegerField()
    agua_req = models.FloatField()

    def __str__(self):
        return self.nombre_planta


class Configuracion(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    precio_maiz = models.FloatField()
    unidadMedidaMaiz = models.CharField(max_length=20)

    def __str__(self):
        return 'Config: %s' %self.usuario


class Fertilizante(models.Model):
    configuracion = models.ForeignKey(Configuracion, null=True, blank=True, on_delete=models.PROTECT)
    nombre_fertilizante = models.CharField(max_length=50)
    porc_nitrogeno = models.FloatField()
    porc_fosforo = models.FloatField()
    porc_potasio = models.FloatField()
    peso = models.FloatField()
    unidadMedidaFert = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_fertilizante


class Simulacion(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    nombre_sim = models.CharField(max_length=50)
    semilla = models.CharField(max_length=50)
    fecha_siembra = models.DateField()
    area = models.FloatField()
    unidad_long = models.CharField(max_length=20, choices=UNIDAD_LONG)
    depto = models.CharField(max_length=20, default="")
    zona = models.CharField(max_length=20, default="")
    tipo_suelo = models.CharField(max_length=50, choices=TIPO_SUELO, null=True, blank=True)
    nivel_p = models.CharField(max_length=20, choices=NIVEL, null=True, blank=True)
    nivel_k = models.CharField(max_length=20, choices=NIVEL, null=True, blank=True)
    compartir = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre_sim


class Aplicacion(models.Model):
    simulacion = models.ForeignKey(Simulacion,null=True, blank=True, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, null=True, blank=True, on_delete=models.CASCADE)
    fertilizante = models.ForeignKey(Fertilizante, null=True, blank=True, on_delete=models.CASCADE)
    fecha_app = models.DateField()
    nitrogeno_req = models.FloatField()
    fosforo_req = models.FloatField()
    potasio_req = models.FloatField()

    def __str__(self):
        return 'aplicacion: %s' %self.planta


class Departamento(models.Model):
    nombre_depto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_depto


class Region(models.Model):
    depto = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
    estacion = models.CharField(max_length=20)
    zona = models.CharField(max_length=20)

    def __str__(self):
        return 'Region: %s' %self.zona


class Humedad(models.Model):
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
    mes = models.IntegerField()
    promedio = models.FloatField()
    acumulado = models.FloatField()

    def __str__(self):
        return 'humedad: %s' %self.region


class Requerimiento(models.Model):
    nitrogeno = models.FloatField()
    fosforo = models.FloatField()
    potasio = models.FloatField()