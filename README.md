# Gestion-de-Tareas

> Sistema de Gestión de Tareas con API REST y SQLite

Este proyecto es una API REST simple desarrollada con Flask que permite el registro y login de usuarios, almacenando la información de forma segura en una base de datos SQLite. Incluye también un cliente de consola para interactuar con la API.

## Requisitos Técnicos

- Python 3.x
- Flask
- Werkzeug (para hasheo de contraseñas)
- Requests (para el cliente)

## Estructura del Proyecto

```
/
|-- database.py         # Script para inicializar la DB
|-- servidor.py         # API Flask
|-- cliente.py          # Cliente de consola
|-- tareas.db           # Archivo de la base de datos SQLite
|-- requirements.txt    # Dependencias
|-- README.md           # Este archivo
```

## Instrucciones de Ejecución

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/nyrha23/Gestion-de-Tareas.git
    cd Gestion-de-Tareas
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows: venv\Scripts\activate
    # En macOS/Linux: source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicializar la base de datos:**
    > Solo necesitas hacerlo una vez
    ```bash
    python database.py
    ```

5.  **Ejecutar el servidor API:**
    > En una terminal
    ```bash
    python servidor.py
    ```
    El servidor estará escuchando en `http://127.0.0.1:5000`.

6.  **Ejecutar el cliente de consola:**
    > En otra terminal en parelelo
    ```bash
    python cliente.py
    ```
    Sigue las instrucciones en el menú interactivo para probar los endpoints.

## Pruebas Realizadas

A continuación se adjuntan capturas de pantalla de las pruebas exitosas:

**1. Registro de un nuevo usuario:** 

![Registro Exitoso](/img/Captura1.jpg)
 
**2. Inicio de sesión correcto:** 

![Login Exitoso](/img/Captura2.jpg)
 
**3. Inicio de sesión con credenciales incorrectas:** 

![Login Fallido](/img/Captura3.jpg)
 
**4. Salir:** 

![Saliendo](/img/Captura4.jpg)
