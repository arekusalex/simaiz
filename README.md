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

#### ###################################################
### CREANDO LA BASE DE DATOS CON POSTGRESQL 


Necesitarán instalar la conexión PSYCOPG2, esto sirve para poder enlazar la conexión entre Django y Postgres

> pip install psycopg2

######################
### LINUX
En Linux utilizaremos la terminal para poder crear la base de datos

###### Instalación de Postgresql
> sudo apt-get install postgresql

##### Abrir la ventana de comandos de Postgres
Una vez instalado postgres es necesario configurarlo
Para ingresar comandos de Postgres es de la siguiente manera

> sudo -i -u postgres

Ingresen la contraseña de superusuario y les aparecerá:

> postgres@user ~ $ 

##### Creando el usuario de Postgres
Ejecutar los siguientes comandos:

> createuser --interactive --pwprompt

Colocan un nombre de usuario:
> miusuariodb

Colocan una contraseña:
> usuariodb

A las preguntas que salgan a continuación esta es la secuencia de respuestas:
> n
> y
> n

##### Creando la base de datos
Le colocamos un nombre a la base de datos, en este caso para el proyecto:

> createdb simaiz_db

Para dar acceso a la base de datos al usuario de Postgres ejecutamos:
> psql

La salida será:
> psql (9.5.11)
> Type "help" for help.
> 
> postgres=#

Después del "#" ejecutamos (darle acceso al usuario a la db):
> grant all privileges on database simaiz_db to miusuariodb

Despues colocamos:
> ;

Le damos enter y aparecerá:

> postgres-# ;
> GRANT
> postgres=#

Salimos:
> \q

##### Salir de Postgres
Ejecutar:
> exit

Habremos vuelto al terminal de Linux



