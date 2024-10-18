"""
Este programa es un sencillo simulador de lanzamiento de dados. El usuario puede especificar cuántos dados desea lanzar, y el programa devolverá los resultados de los lanzamientos.

Uso:
- Ejecuta el programa.
- Cuando se te solicite, introduce la cantidad de dados que deseas lanzar.
- Para salir del juego, escribe 'salir'.
- El programa mostrará los resultados de los lanzamientos.

¡Diviértete!
"""

import random

# Función para lanzar dados y devolver los resultados en una lista
def lanzar_dados(cantidad: int = 2) -> list[int]:
    """
    Lanza varios dados y devuelve los resultados en una lista.

    :param cantidad: La cantidad de dados a lanzar.
    :return: Una lista con los resultados de los lanzamientos.
    """
    if cantidad <= 0:
        # Si la cantidad es menor o igual a cero, se lanza un error
        raise ValueError

    resultados: list[int] = []
    for i in range(cantidad):
        # Generamos un número aleatorio entre 1 y 6 para simular el lanzamiento de un dado
        dado: int = random.randint(1, 6)
        resultados.append(dado)

    return resultados

# Función principal del programa
def main():
    while True:
        try:
            # Solicitamos al usuario que introduzca la cantidad de dados a lanzar
            entrada_usuario: str = input('¿Cuántos dados te gustaría lanzar? ')

            # Para salir del juego
            if entrada_usuario.lower() == 'salir':
                print('¡Gracias por jugar!')
                break

            # Intentamos convertir la entrada del usuario a entero y lanzamos los dados
            print(*lanzar_dados(int(entrada_usuario)), sep=', ')
        except ValueError:
            # Si ocurre un error, informamos al usuario
            print('(Por favor, introduce un número válido)')

# Ejecutamos la función principal
if __name__ == '__main__':
    main()
