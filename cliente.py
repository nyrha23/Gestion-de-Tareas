# cliente.py
import requests
import getpass # Oculta la contraseña al escribirla

BASE_URL = 'http://127.0.0.1:5000' # Dirección donde corre la API Flask

def registrar_usuario():
  usuario = input("Ingrese su nuevo nombre de usuario: ")
  contrasenia = getpass.getpass("Ingrese su nueva contraseña: ")
  
  url = f"{BASE_URL}/registro"
  datos = {"usuario": usuario, "contraseña": contrasenia}
  
  try:
    respuesta = requests.post(url, json=datos)
    print("Respuesta del servidor:", respuesta.json())
  except requests.exceptions.ConnectionError as e:
    print(f"Error de conexión: No se pudo conectar al servidor en {BASE_URL}")

def iniciar_sesion():
  usuario = input("Ingrese su nombre de usuario: ")
  contrasenia = getpass.getpass("Ingrese su contraseña: ")
    
  url = f"{BASE_URL}/login"
  datos = {"usuario": usuario, "contraseña": contrasenia}

  try:
    respuesta = requests.post(url, json=datos)
    print("Respuesta del servidor:", respuesta.json())
  except requests.exceptions.ConnectionError as e:
    print(f"Error de conexión: No se pudo conectar al servidor en {BASE_URL}")

def ver_bienvenida_tareas():
  url = f"{BASE_URL}/tareas"
  print(f"\nAccediendo a {url}...")
  print("Esta es una página de bienvenida pública.")
  print("En una aplicación real, se requeriría un token de sesión para ver tareas personales.\n")
  # En un cliente de consola, no es práctico renderizar HTML.
  # Simplemente confirma que se puede acceder.
  try:
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
      print("Éxito: Se recibió una respuesta correcta (código 200) de /tareas.")
    else:
      print(f"Error: Se recibió un código de estado inesperado: {respuesta.status_code}")
  except requests.exceptions.ConnectionError as e:
    print(f"Error de conexión: No se pudo conectar al servidor en {BASE_URL}")


def main():
  while True:
    print("\n--- Cliente del Sistema de Tareas ---")
    print("1. Registrar un nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Ver página de bienvenida de tareas")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
      registrar_usuario()
    elif opcion == '2':
      iniciar_sesion()
    elif opcion == '3':
      ver_bienvenida_tareas()
    elif opcion == '4':
      print("Saliendo...")
      break
    else:
      print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
  main()
