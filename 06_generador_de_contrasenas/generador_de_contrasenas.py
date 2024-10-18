"""
Este programa es un generador de contraseñas que crea contraseñas aleatorias basadas en las especificaciones del usuario.

Uso:
- El programa genera 5 contraseñas aleatorias con una longitud de 15 caracteres.
- Las contraseñas pueden incluir letras mayúsculas, símbolos y dígitos.
- Cada contraseña generada muestra si contiene letras mayúsculas y símbolos.

¡Utiliza este generador para crear contraseñas seguras y aleatorias!
"""

import string
import secrets

# Función que verifica si una contraseña contiene letras mayúsculas
def contiene_mayusculas(contraseña: str) -> bool:
    """Verifica si una contraseña contiene caracteres en mayúscula"""

    for caracter in contraseña:
        if caracter.isupper():
            return True

    return False  # No se encontraron caracteres en mayúscula

# Función que verifica si una contraseña contiene símbolos
def contiene_simbolos(contraseña: str) -> bool:
    """Verifica si una contraseña contiene símbolos"""

    for caracter in contraseña:
        if caracter in string.punctuation:
            return True

    return False  # No se encontraron símbolos

# Función que genera una contraseña basada en las especificaciones del usuario
def generar_contraseña(longitud: int, simbolos: bool, mayusculas: bool) -> str:
    """
    Genera una contraseña basada en las especificaciones del usuario

    :param longitud: La longitud de la contraseña
    :param simbolos: Indica si la contraseña debe incluir símbolos
    :param mayusculas: Indica si la contraseña debe incluir letras mayúsculas
    :return: str
    """

    # Creamos una combinación de caracteres para elegir
    combinacion: str = string.ascii_lowercase + string.digits

    # Si el usuario quiere símbolos, agregamos puntuación a la combinación
    if simbolos:
        combinacion += string.punctuation

    # Si el usuario quiere mayúsculas, agregamos letras mayúsculas a la combinación
    if mayusculas:
        combinacion += string.ascii_uppercase

    # Obtenemos la longitud de la combinación de caracteres
    longitud_combinacion: int = len(combinacion)

    # Creamos una variable para almacenar la nueva contraseña
    nueva_contraseña: str = ''

    # Añadimos un nuevo carácter aleatorio a la contraseña en cada iteración
    for _ in range(longitud):
        nueva_contraseña += combinacion[secrets.randbelow(longitud_combinacion)]

    return nueva_contraseña

# Punto de entrada del programa
if __name__ == '__main__':
    # Generamos 5 contraseñas aleatorias
    for i in range(1, 6):
        nueva_pass: str = generar_contraseña(longitud=15, simbolos=True, mayusculas=True)
        especificaciones: str = f'Mayúsculas: {contiene_mayusculas(nueva_pass)}, Símbolos: {contiene_simbolos(nueva_pass)}'

        # Imprimimos el número de contraseña, la contraseña en sí y sus características
        print(f'{i} -> {nueva_pass} ({especificaciones})')
