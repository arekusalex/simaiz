from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Suelo(models.Model):
    nombre_suelo = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre_suelo), self.nombre_suelo

class Elemento(models.Model):
    nombre_elemento = models.CharField(max_length=20)
    simbolo = models.CharField(max_length=2)

    def __str__(self):
        return self.nombre_elemento

class Planta(models.Model):
    nombre_planta = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    dias_ciclo = models.IntegerField()
    agua_req = models.FloatField()

    def __str__(self):
        return '{}'.format(self.nombre_planta), self.nombre_planta

class UnidadMedida(models.Model):
    unidad_medida = models.CharField(max_length=20)
    prefijo=models.CharField(max_length=5)

    def __str__(self):
        return '{}'.format(self.unidad_medida), self.prefijo

class Configuracion(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    precio_maiz = models.FloatField()

    def __str__(self):
        return 'Config: %s' %self.usuario

class Fertilizante(models.Model):
    configuracion = models.ForeignKey(Configuracion, null=True, blank=True, on_delete=models.CASCADE)
    nombre_fertilizante = models.CharField(max_length=50)
    tipo_fertilizante = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre_fertilizante), self.nombre_fertilizante

class Contenido(models.Model):
    fertilizante = models.ForeignKey(Fertilizante, null=True, blank=True, on_delete=models.CASCADE)
    elemento = models.OneToOneField(Elemento, null=True, blank=True, on_delete=models.CASCADE)
    suelo = models.ForeignKey(Suelo, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=20)
    porcentaje = models.FloatField()

    def __str__(self):
        return 'contenido: %s -> %s' %self.fertilizante %self.elemento

class Simulacion(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, null=True, blank=True, on_delete=models.CASCADE)
    nombre_sim = models.CharField(max_length=50)
    fecha_siembra = models.DateField()
    rendimiento = models.FloatField()
    total = models.FloatField()
    compartir = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_sim

class Departamento(models.Model):
    nombre_depto = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.nombre_depto), self.nombre_depto

class Terreno(models.Model):
    depto = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
    suelo = models.OneToOneField(Suelo, null=True, blank=True, on_delete=models.CASCADE)
    unidad = models.OneToOneField(UnidadMedida, null=True, blank=True, on_delete=models.CASCADE)
    area = models.FloatField()

    def __str__(self):
        return 'suelo %s' %self.depto

class Aplicacion(models.Model):
    simulacion= models.ForeignKey(Simulacion,null=True, blank=True, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, null=True, blank=True, on_delete=models.CASCADE)
    fertilizante = models.ForeignKey(Fertilizante, null=True, blank=True, on_delete=models.CASCADE)
    terreno = models.ForeignKey(Terreno, null=True, blank=True, on_delete=models.CASCADE)
    cantidad_fertilizante = models.FloatField(null=True)
    fecha = models.DateField()
    nitrogeno_req = models.FloatField()
    fosforo_req = models.FloatField()
    potasio_req = models.FloatField()

    def __str__(self):
        return 'aplicacion: %s' %self.planta

class Region(models.Model):
    depto = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
    estacion = models.CharField(max_length=20)
    zona = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.zona), 'Region: %s' %self.depto

class Humedad(models.Model):
    depto = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
    mes = models.CharField(max_length=15)
    valor = models.FloatField()
    promedio = models.FloatField()
    porcentaje = models.FloatField()

    def __str__(self):
        return 'humedad: %s' %self.depto
