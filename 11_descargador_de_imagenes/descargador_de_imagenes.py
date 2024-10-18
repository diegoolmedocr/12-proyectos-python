"""
Este programa descarga imágenes desde una URL proporcionada por el usuario y las guarda en su computadora local.

Uso:
- Ejecuta el programa.
- Cuando se te solicite, introduce la URL de la imagen que deseas descargar.
- Introduce el nombre con el que deseas guardar la imagen.
- La imagen se descargará y se guardará en la carpeta especificada (por defecto, 'images').

¡Disfruta descargando tus imágenes!
"""

import os
import requests

# Función para obtener la extensión de la imagen a partir de la URL
def obtener_extension(url_imagen: str) -> str | None:
    # Creamos una lista de extensiones populares para verificar
    extensiones: list[str] = ['.png', '.jpg', '.jpeg', '.gif', '.svg']

    # Verificamos que la extensión exista dentro de la URL
    for ext in extensiones:
        if ext in url_imagen:
            return ext
    # Si no se encuentra ninguna extensión, la función retorna None

# Función para descargar la imagen desde la URL proporcionada
def descargar_imagen(url_imagen: str, nombre: str, carpeta: str = None):
    """Descarga una imagen desde cualquier URL dada"""

    # Intentamos obtener la extensión correcta de la imagen desde la URL
    if ext := obtener_extension(url_imagen):
        if carpeta:
            # Si se especifica una carpeta, construimos la ruta incluyendo la carpeta
            nombre_imagen: str = f'{carpeta}/{nombre}{ext}'
        else:
            # Si no hay carpeta especificada, usamos el nombre directamente
            nombre_imagen: str = f'{nombre}{ext}'
    else:
        # Si no se pudo obtener la extensión, lanzamos una excepción
        raise Exception('No se pudo localizar la extensión de la imagen...')

    # Verificamos si el archivo ya existe para evitar sobrescribirlo
    if os.path.isfile(nombre_imagen):
        raise Exception('El nombre del archivo ya existe...')

    try:
        # Obtenemos el contenido de la imagen en bytes desde la URL
        contenido_imagen: bytes = requests.get(url_imagen).content
        # Escribimos los bytes de la imagen en un archivo local
        with open(nombre_imagen, 'wb') as handler:
            handler.write(contenido_imagen)
            print(f'¡Descargado: "{nombre_imagen}" exitosamente!')
    except Exception as e:
        # Manejamos cualquier excepción que ocurra durante la descarga
        print(f'Error: {e}')

# Punto de entrada del programa
if __name__ == '__main__':
    # URLs de muestra (comentadas)
    # url_imagen_1: str = 'https://media.istockphoto.com/id/184276818/photo/red-apple.jpg'  # NOQA
    # url_imagen_2: str = 'https://w.wallhaven.cc/full/1p/wallhaven-1p398w.jpg'
    # url_imagen_3: str = 'https://www.svgrepo.com/show/376344/python.svg'

    # Solicitamos al usuario que introduzca la URL de la imagen
    entrada_url: str = input('Introduce una URL: ')
    # Solicitamos al usuario que introduzca el nombre con el que desea guardar la imagen
    entrada_nombre: str = input('¿Cómo te gustaría nombrar el archivo?: ')

    # Descargamos la imagen usando los datos proporcionados por el usuario
    print('Descargando...')
    descargar_imagen(entrada_url, nombre=entrada_nombre, carpeta='images')
