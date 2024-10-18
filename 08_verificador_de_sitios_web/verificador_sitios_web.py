"""
Este programa es una herramienta que verifica el estado de varios sitios web. Lee una lista de sitios web desde un archivo CSV, realiza solicitudes HTTP a cada uno y muestra el código de estado junto con una descripción legible.

Uso:
- Asegúrate de tener un archivo 'websites.csv' que contenga los sitios web que deseas verificar, uno por línea.
- Ejecuta el programa.
- El programa mostrará el estado de cada sitio web de la lista.

Nota:
- Necesitas instalar las bibliotecas 'requests' y 'fake_useragent' para que el programa funcione correctamente.
  Puedes instalarlas usando 'pip install requests fake-useragent'.

¡Disfruta monitoreando tus sitios web!
"""

import csv
import requests
from http import HTTPStatus
from fake_useragent import UserAgent

# Función que carga los sitios web desde un archivo CSV
def obtener_sitios_web(ruta_csv: str) -> list[str]:
    """Carga sitios web desde un archivo CSV"""

    sitios_web: list[str] = []
    with open(ruta_csv, 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            # Aseguramos que la URL tenga 'https://'
            if 'https://' not in fila[1]:
                sitios_web.append(f'https://{fila[1]}')
            else:
                sitios_web.append(fila[1])

    return sitios_web

# Función que obtiene un agente de usuario para usar en las solicitudes
def obtener_user_agent() -> str:
    """Devuelve un agente de usuario que se puede usar con requests"""

    ua = UserAgent()
    return ua.chrome

# Función que obtiene una descripción legible del código de estado HTTP
def obtener_descripcion_estado(codigo_estado: int) -> str:
    """Usa el código de estado para devolver una descripción legible"""

    for valor in HTTPStatus:
        if valor == codigo_estado:
            descripcion: str = f'({valor} {valor.name}) {valor.description}'
            return descripcion

    return '(???) Código de estado desconocido...'

# Función que verifica el estado de un sitio web y muestra el resultado
def verificar_sitio_web(sitio_web: str, user_agent: str):
    """Obtiene el código de estado de un sitio web y muestra el resultado"""
    try:
        # Realizamos una solicitud GET al sitio web con el agente de usuario especificado
        codigo: int = requests.get(sitio_web, headers={'User-Agent': user_agent}).status_code
        print(sitio_web, obtener_descripcion_estado(codigo))
    except Exception:
        # Manejo de excepciones en caso de que no se pueda acceder al sitio web
        print(f'**No se pudo obtener información para el sitio web: "{sitio_web}"')

# Función principal del programa
def main():
    # Obtenemos la lista de sitios web desde el archivo CSV
    sitios: list[str] = obtener_sitios_web('websites.csv')
    user_agent: str = obtener_user_agent()

    # Verificamos cada sitio web en la lista
    for i, sitio in enumerate(sitios):
        verificar_sitio_web(sitio, user_agent)

# Ejecutamos la función principal si el script se ejecuta directamente
if __name__ == '__main__':
    main()
