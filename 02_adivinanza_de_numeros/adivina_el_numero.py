"""
Este programa es un sencillo juego de "Adivina el Número" en el que el usuario debe adivinar un número aleatorio generado por el programa dentro de un rango especificado.

Uso:
- Ejecuta el programa.
- Introduce tus conjeturas cuando se te solicite.
- El programa te dará pistas indicando si el número es mayor o menor.
- Continúa hasta que adivines el número correcto.

¡Buena suerte!
"""

from random import randint

# Configuración inicial del programa
numero_inferior, numero_superior = 1, 10
# Generamos un número aleatorio dentro del rango especificado
numero_aleatorio: int = randint(numero_inferior, numero_superior)
print(f'Adivina el número en el rango de {numero_inferior} a {numero_superior}.')

# Ejecutamos un bucle infinito para el juego
while True:
    # Obtenemos la conjetura del usuario
    try:
        conjetura_usuario: int = int(input('Adivina: '))
    except ValueError as e:
        # Manejo de excepción si el usuario introduce un valor no numérico
        print('Por favor, introduce un número válido.')
        continue

    # Comprobamos la conjetura del usuario
    if conjetura_usuario > numero_aleatorio:
        print('El número es menor.')
    elif conjetura_usuario < numero_aleatorio:
        print('El número es mayor.')
    else:
        # El usuario ha adivinado correctamente
        print('¡Has adivinado el número!')
        break
