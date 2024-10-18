"""
Este programa intenta encontrar una contraseña utilizando dos métodos:
1. Busca la contraseña en una lista de palabras comunes.
2. Si no la encuentra, utiliza un método de fuerza bruta para adivinarla.

Uso:
- Definir la contraseña en la variable `password` en la función `main`.
- El programa primero intentará encontrar la contraseña en el archivo `words.text`.
- Si no la encuentra, intentará adivinarla utilizando combinaciones de caracteres.
"""

import itertools
import string
import time

def adivinanza_comun(palabra: str) -> str | None:
    """Verifica un archivo lleno de palabras comunes"""

    # Abre el archivo 'words.text' en modo lectura
    with open('words.text', 'r') as palabras:
        # Lee todas las líneas del archivo y las guarda en una lista
        lista_palabras: list[str] = palabras.read().splitlines()

    # Itera sobre la lista de palabras comunes
    for i, coincidencia in enumerate(lista_palabras, start=1):
        if coincidencia == palabra:
            return f'Coincidencia común: {coincidencia} (#{i})'

# Recorre todas las combinaciones de caracteres
def fuerza_bruta(palabra: str, longitud: int, digitos=False, simbolos=False) -> str | None:
    """Realiza fuerza bruta para encontrar una palabra"""

    # Modificar esto para incluir todos los símbolos
    caracteres: str = string.ascii_lowercase

    if digitos:
        caracteres += string.digits

    if simbolos:
        caracteres += string.punctuation

    intentos: int = 0
    # Genera todas las combinaciones posibles de caracteres de la longitud especificada
    for intento in itertools.product(caracteres, repeat=longitud):
        intentos += 1
        intento: str = ''.join(intento)

        if intento == palabra:
            return f'"{palabra}" fue encontrada en {intentos:,} intentos.'
        # print(intento, intentos) # Descomentar esto cuando estés probando

def main():
    print('Buscando...')
    contrasena: str = 'pass1'

    # Obtiene el tiempo de inicio
    tiempo_inicio: float = time.perf_counter()

    # Busca palabras comunes antes de usar la fuerza bruta
    if coincidencia_comun := adivinanza_comun(contrasena):
        print(coincidencia_comun)
    else:
        if encontrada := fuerza_bruta(contrasena, longitud=5, digitos=True, simbolos=False):
            print(encontrada)
        else:
            print('No hubo coincidencia...')

    # Obtiene el tiempo de finalización
    tiempo_fin: float = time.perf_counter()

    # Muestra el tiempo que tomó
    print(round(tiempo_fin - tiempo_inicio, 2), 's')

if __name__ == '__main__':
    main()