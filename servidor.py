# servidor.py
from flask import Flask, request, jsonify, render_template_string
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Inicializa la aplicación Flask
app = Flask(__name__)
DATABASE = 'tareas.db'

# Función para conectar a la base de datos
def get_db_connection():
  conn = sqlite3.connect(DATABASE)
  conn.row_factory = sqlite3.Row # Permite acceder a las columnas por nombre
  return conn

# Endpoint de Registro de Usuarios
@app.route('/registro', methods=['POST'])
def registro():
  # Obtiene los datos del JSON de la solicitud
  datos = request.get_json()
  if not datos or 'usuario' not in datos or 'contrasenia' not in datos:
    return jsonify({"mensaje": "Datos incompletos"}), 400

  usuario = datos['usuario']
  contrasenia = datos['contrasenia']

  # Hashear la contraseña antes de guardarla
  contrasenia_hash = generate_password_hash(contrasenia)

  conn = get_db_connection()
  cursor = conn.cursor()

  try:
    # Inserta el nuevo usuario en la base de datos: 201 Created y 409 Conflict
    cursor.execute("INSERT INTO usuarios (usuario, contrasenia_hash) VALUES (?, ?)", (usuario, contrasenia_hash))
    conn.commit()
    mensaje = f"Usuario '{usuario}' registrado exitosamente."
    status_code = 201
  except sqlite3.IntegrityError:
    # Esto ocurre si el usuario ya existe (debido a la restricción de UNIQUE)
    mensaje = f"El usuario '{usuario}' ya existe."
    status_code = 409
  finally:
    conn.close()

  return jsonify({"mensaje": mensaje}), status_code

# Endpoint de Inicio de Sesión: 400 
@app.route('/login', methods=['POST'])
def login():
  datos = request.get_json()
  if not datos or 'usuario' not in datos or 'contrasenia' not in datos:
    return jsonify({"mensaje": "Datos incompletos"}), 400

  usuario_ingresado = datos['usuario']
  contrasenia_ingresada = datos['contrasenia']

  conn = get_db_connection()
  cursor = conn.cursor()
  
  # Buscar al usuario en la base de datos
  cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario_ingresado,))
  usuario_db = cursor.fetchone()
  conn.close()

  if usuario_db and check_password_hash(usuario_db['contrasenia_hash'], contrasenia_ingresada):
    # Si el usuario existe y la contraseña es correcta: 200 Authorized
    return jsonify({"mensaje": f"Inicio de sesión exitoso. ¡Bienvenido, {usuario_ingresado}!"}), 200
  else:
    # Si el usuario no existe o la contraseña es incorrecta: 401 Unauthorized
    return jsonify({"mensaje": "Credenciales inválidas"}), 401 

# Endpoint de Gestión de Tareas (Bienvenida)
# En una app real, este endpoint estaría protegido y requeriría autenticación.
@app.route('/tareas', methods=['GET'])
def get_tareas():
  # Por ahora, solo muestra un mensaje de bienvenida en HTML.
  # En un futuro, aquí se mostrarían las tareas del usuario autenticado.
  html_bienvenida = """
  <!DOCTYPE html>
  <html>
  <head>
    <title>Gestión de Tareas</title>
    <style>
      body { font-family: sans-serif; text-align: center; margin-top: 50px; }
      h1 { color: #333; }
      </style>
  </head>
  <body>
    <h1>¡Bienvenido a Gestión de Tareas!</h1>
    <p>Este es el punto de partida. ¡Felicidades por llegar hasta aquí!</p>
  </body>
  </html>
  """
  return render_template_string(html_bienvenida)

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
  # debug=True permite ver los errores y recarga el servidor automáticamente con los cambios
  app.run(debug=True)
