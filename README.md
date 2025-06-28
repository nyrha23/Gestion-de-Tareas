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

---

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

---

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

---

## Conceptos Fundamentales
> Esta sección explica las decisiones técnicas clave tomadas durante el desarrollo del proyecto.

### ¿Por qué hashear contraseñas?

Hashear contraseñas es una práctica de seguridad fundamental e innegociable. La razón principal es proteger la información del usuario en caso de una brecha de seguridad.

* **Nunca almacenar texto plano**: Si un atacante logra acceder a tu base de datos y las contraseñas están en texto plano (p. ej., "1234"), obtiene inmediatamente acceso a todas las cuentas. Peor aún, como muchos usuarios reutilizan contraseñas, el atacante podría intentar usar esa misma combinación en otros servicios (Gmail, bancos, etc.).

* **El hasheo es una vía de un solo sentido**: Una función de hash (como la que usa `werkzeug.security`) convierte una entrada (la contraseña) en una cadena de caracteres de longitud fija (el hash). Este proceso es irreversible; no se puede "des-hashear" para obtener la contraseña original.

* **Proceso de verificación**: Cuando un usuario inicia sesión, no comparas la contraseña guardada. En su lugar, tomas la contraseña que el usuario ingresó, le aplicas la misma función de hash y comparas el resultado con el hash almacenado en la base de datos. Si los hashes coinciden, la contraseña es correcta.

En resumen, hashear protege contra el robo de credenciales, salvaguardando la privacidad y seguridad de los usuarios más allá de la aplicación.

### Ventajas de usar SQLite en este proyecto

Para un proyecto de esta escala (un sistema de gestión de tareas simple, con un solo desarrollador y para fines de aprendizaje), SQLite ofrece varias ventajas significativas sobre sistemas de bases de datos más complejos como PostgreSQL o MySQL:

* **Cero Configuración (Serverless)**: SQLite no requiere un proceso de servidor separado. La base de datos es un simple archivo (`.db`) en el disco. Esto elimina la necesidad de instalar, configurar y mantener un servicio de base de datos, lo que simplifica enormemente el desarrollo y el despliegue.

* **Portabilidad**: Como la base de datos completa está contenida en un único archivo, es increíblemente fácil de copiar, mover y compartir. Se puede simplemente enviar el archivo `tareas.db` a otra persona, y funcionará sin más.

* **Integración nativa con Python**: La librería `sqlite3` viene incluida en la biblioteca estándar de Python, por lo que no se necesita instalar controladores o conectores adicionales para empezar a trabajar.

* **Ideal para Prototipado y Proyectos Pequeños**: Su simplicidad y rapidez de configuración la hacen perfecta para desarrollar prototipos, aplicaciones de escritorio, o aplicaciones web con tráfico bajo a moderado, como es el caso de este proyecto.

En conclusión, SQLite fue la elección perfecta aquí porque minimiza la complejidad y permite centrarse en aprender la lógica de la API, la gestión de datos y la seguridad, sin la sobrecarga de administrar un sistema de base de datos cliente-servidor.
