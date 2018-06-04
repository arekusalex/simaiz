from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Suelo)
admin.site.register(Planta)
admin.site.register(Configuracion)
admin.site.register(Fertilizante)
admin.site.register(Simulacion)
admin.site.register(Aplicacion)
admin.site.register(Condiciones)

admin.site.register(Requerimiento)
admin.site.register(Departamento)
admin.site.register(Region)
admin.site.register(Humedad)
