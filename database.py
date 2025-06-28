# database.py
import sqlite3

# Conecta a la base de datos (se creará si no existe)
conn = sqlite3.connect('tareas.db')

# Crea un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crea la tabla de usuarios si no existe
# - id: Clave primaria autoincremental
# - usuario: Nombre de usuario, debe ser único
# - contrasenia_hash: Almacenará la contraseña hasheada
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    contrasenia_hash TEXT NOT NULL
)
''')

# Guarda los cambios y cierra la conexión
conn.commit()
conn.close()

print("Base de datos 'tareas.db' y tabla 'usuarios' creadas exitosamente.")
