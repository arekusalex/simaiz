# SIMAIZ
## Sistema de simulacion del ciclo de cultivo del maiz. 
Tarea ex-aula de Herramientas de Productividad

### Intengrantes
| ALUMNO | CARNET |
|--|--|
| Amaya Palacios, Edwin Joel | AP16014 |
| Cortez Dominguez, Luis Miguel | CD13001 |
| Leiva Pérez, Edwin Alexander | LP14005 |
| Presa Mariona, José Rodrigo | PM15007 |


### ¿Cómo crear entorno virtual para el proyecto ? (python 3.x)
Despues de haber clonado el proyecto, se van a la ruta donde lo clonaron y alli habren un consola del sistema y crear un entorno virtual asi:
#### Windows
> virtualenv .simaiz

#### Linux
> python3 -m venv .simaiz

 Luego para activar el entorno se diriguen a la carpeta .simaiz\Scripts si estan en windows pero si estan en linuz .simaiz/bin/ y lo activan de la siguiente manera:
 #### Windows 
 >activate

#### Linux
> source activate

Ahora nos salimos de la carpeta a la altura de la carpeta simaiz

---> simaiz                                                               
------>.simaiz/                                                  
------>simaiz/                                                   
------>.git/                                               
------>.gitignore                                       
------>.README.md                                              
------>.requirements.txt                                       

### Instalando dependencias del proyecto
Para instalar las dependencias del proyecto se necesita del archivo **requirements.txt** para hacer es con el siguiente comando:
> pip install -r requirements.txt

Y ya con ese comando se empezaran a descargar las dependencias del proyecto y prodremos empezar a programar.

##### Desactivar entorno virtual
Windows y Linux
>deactivate