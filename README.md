# Custom Login
App de prueba para autenticacion y autorizacion.

## Librerias
Utiliza Python 2.7, PostgreSQL, Pyramid, SQLAlchemy, Jinja2

## Requerimientos
* Python 2.7
* PostgreSQL

## Instalacion
* Crear una base de datos PostgreSQL
* Modificar **development.ini** cambiando la variable **sqlalchemy.url** con los datos de la nueva base
* Ejecutar el comando **initialize_db development.ini** para crear un usuario de prueba
* Ingresar a http://localhost:8000/login
