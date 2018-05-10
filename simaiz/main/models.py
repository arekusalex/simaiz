from django.db import models

# Create your models here.

class Suelo(models.Model):
    nombre_suelo = models.CharField(max_length=50)

class Elemento(models.Model):
    nombre_elemento = models.CharField(max_length=20)
    simbolo = models.CharField(max_length=2)

class Planta(models.Model):
    nombre_planta = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    dias_ciclo = models.IntegerField()
    agua_req = models.FloatField()

class UnidadMedida(models.Model):
    unidad_medida = models.CharField(max_length=20)

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

class Configuracion(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    precio_maiz = models.FloatField()

class Fertilizante(models.Model):
    configuracion = models.ForeignKey(Configuracion, null=True, blank=True, on_delete=models.CASCADE)
    nombre_fertilizante = models.CharField(max_length=50)
    tipo_fertilizante = models.CharField(max_length=50)

class Contenido(models.Model):
    fertilizante = models.ForeignKey(Fertilizante, null=True, blank=True, on_delete=models.CASCADE)
    elemento = models.OneToOneField(Elemento, null=True, blank=True, on_delete=models.CASCADE)
    suelo = models.ForeignKey(Suelo, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=20)
    porcentaje = models.FloatField()

class Simulacion(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    planta = models.OneToOneField(Planta, null=True, blank=True, on_delete=models.CASCADE)
    nombre_sim = models.CharField(max_length=50)
    fecha_siembra = models.DateField()
    rendimiento = models.FloatField()
    total = models.FloatField()
    compartir = models.BooleanField(default=False)

class Aplicacion(models.Model):
    planta = models.ForeignKey(Planta, null=True, blank=True, on_delete=models.CASCADE)
    fertilizante = models.ForeignKey(Fertilizante, null=True, blank=True, on_delete=models.CASCADE)
    cantidad_fertilizante = models.FloatField()
    fecha = models.DateField()
    nitrogeno_req = models.FloatField()
    fosforo_req = models.FloatField()
    potasio_req = models.FloatField()

class Terreno(models.Model):
    suelo = models.OneToOneField(Suelo, null=True, blank=True, on_delete=models.CASCADE)
    unidad = models.OneToOneField(UnidadMedida, null=True, blank=True, on_delete=models.CASCADE)
    area = models.FloatField()

class Departamento(models.Model):
    terreno = models.OneToOneField(Terreno, null=True, blank=True, on_delete=models.CASCADE)
    nombre_depto = models.CharField(max_length=20)

class Region(models.Model):
    depto = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
    estacion = models.CharField(max_length=20)
    zona = models.CharField(max_length=20)

class Humedad(models.Model):
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
    mes = models.CharField(max_length=15)
    valor = models.FloatField()
    promedio = models.FloatField()
    porcentaje = models.FloatField()





