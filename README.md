# Biblioteca
Aplicacion CRUD de biblioteca

## Instalacion

### Paso 1: Gt clone al proyecto en la carpeta deseada
    git clone https://github.com/hilario-wh/biblioteca.git
### Paso 2: Creacion del entorno en la carpeta deseada
    mkvirtualenv envbiblioteca -p=2.7
### Paso 3: Iniciar el entorno
#### Con virtualenvwrapper
    workon envbiblioteca
#### ó con virtualenv
    source bin/activate
#### Confirmar que sea en python 2.7
    python -V
### Paso 4: instalamos dependencias en el entorno virtual (En el directorio del proyecto)
    pip install  -r requirements.txt
### Paso 5: Crear migraciones: (En el directorio del proyecto)
    python manage.py migrate
#### Paso Opcional: Crear usuario administrador
    python manage.py createsuperuser
### Paso 6: Iniciar el proyecto: (En el directorio del proyecto)
    python manage.py runserver