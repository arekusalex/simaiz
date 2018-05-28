from django.contrib import admin
from .models import Suelo
from .models import Elemento
from .models import Planta
from .models import UnidadMedida
from .models import Configuracion
from .models import Fertilizante
from .models import Contenido
from .models import Simulacion
from .models import Aplicacion
from .models import Terreno
from .models import Departamento
from .models import Region
from .models import Humedad

# Register your models here.
admin.site.register(Suelo)
admin.site.register(Elemento)
admin.site.register(Planta)
admin.site.register(UnidadMedida)
admin.site.register(Configuracion)
admin.site.register(Fertilizante)
admin.site.register(Contenido)
admin.site.register(Simulacion)
admin.site.register(Aplicacion)
admin.site.register(Terreno)
admin.site.register(Departamento)
admin.site.register(Region)
admin.site.register(Humedad)
