from django.db import models

# Create your models here.

class Fertilizante(models.Model):
    nombre_fertilizante = models.CharField(max_length=50)
    tipo_fertilizante = models.CharField(max_length=50)

class Suelo(models.Model):
    nombre_suelo = models.CharField(max_length=50)

class Elemento(models.Model):
    nombre_elemento = models.CharField(max_length=20)
    simbolo = models.CharField(max_length=2)

class Contenido(models.Model):
    elemento = models.OneToOneField(Elemento, null=True, blank=True, on_delete=models.CASCADE)
    fertilizante = models.ForeignKey(Fertilizante, null=True, blank=True, on_delete=models.CASCADE)
    suelo = models.ForeignKey(Suelo, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=20)
    porcentaje = models.FloatField()

class Region(models.Model):
    estacion = models.CharField(max_length=20)
    zona = models.CharField(max_length=20)

class Humedad(models.Model):
    mes = models.CharField(max_length=15)
    valor = models.FloatField()
    promedio = models.FloatField()
    porcentaje = models.FloatField()

class UnidadMedida(models.Model):
    unidad_medida = models.CharField(max_length=20)

class Departamento(models.Model):
    nombre_depto = models.CharField(max_length=20)

class Terreno(models.Model):
    suelo = models.OneToOneField(Suelo, null=True, blank=True, on_delete=models.CASCADE)
    unidad = models.OneToOneField(UnidadMedida, null=True, blank=True, on_delete=models.CASCADE)
    area = models.FloatField()

