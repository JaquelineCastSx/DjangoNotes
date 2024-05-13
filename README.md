# DjangoNotes
# Mynotes Proyect

### **Configuración del Entorno**

Para configurar el entorno de desarrollo y ejecutar el proyecto **`project_notes`**, se deben seguir los siguientes pasos:

1. **Instalación de Python y Django:**
Es necesario tener instalado Python en el sistema. Se puede descargar desde [python.org](https://www.python.org/downloads/). Luego, se instala Django utilizando pip, el gestor de paquetes de Python:
    
    ```bash
    bashCopy code
    pip install django
    
    ```
    
2. **Clonar el Repositorio:**
El usuario debe dirigirse al directorio deseado para almacenar el proyecto y clonar el repositorio de **`project_notes`** desde su ubicación en línea. Luego, debe ingresar al directorio clonado:
    
    ```bash
    bashCopy code
    cd ruta_de_tu_carpeta
    git clone <https://github.com/JaquelineCastSx/DjangoNotes.git>
    cd project_notes
    
    ```
    
3. **Instalación de Dependencias:**
Una vez dentro del directorio del proyecto, se instalan las dependencias necesarias utilizando pip:
    
    ```bash
    bashCopy code
    pip install -r requirements.txt
    
    ```
    

### **Ejecución del Servidor**

Para ejecutar el servidor de desarrollo y comenzar a trabajar en el proyecto, se deben realizar los siguientes pasos:

1. **Configuración de la Base de Datos:**
Antes de iniciar el servidor, es importante configurar la base de datos. Desde el directorio **`project_notes`**, se ejecutan los comandos para realizar las migraciones de la base de datos:
    
    ```bash
    bashCopy code
    python manage.py makemigrations
    python manage.py migrate
    
    ```
    
2. **Iniciar el Servidor:**
Una vez aplicadas las migraciones, se puede iniciar el servidor de desarrollo utilizando el siguiente comando:
    
    ```bash
    bashCopy code
    python manage.py runserver
    
    ```
    
    Esto iniciará el servidor en **`http://127.0.0.1:8000/`** por defecto.
    

Con estos pasos, el usuario puede configurar y ejecutar el proyecto Django **`project_notes`**

### **Ejecución de Casos de Prueba**

Para ejecutar los casos de prueba de la aplicación **`mynotes`**, se verifica estar en el directorio raíz del proyecto **`project_notes`** y utilizar el siguiente comando:

```bash
bashCopy code
python manage.py test mynotes

```

Este comando ejecutará todos los casos de prueba definidos en el módulo **`tests.py`** dentro de la aplicación **`mynotes`**.
