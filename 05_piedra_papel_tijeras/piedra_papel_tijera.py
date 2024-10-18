"""
Este programa es un sencillo juego de "Piedra, Papel o Tijeras" en el que el usuario juega contra la computadora.

Uso:
- Ejecuta el programa.
- Cuando se te solicite, elige entre 'piedra', 'papel' o 'tijeras'.
- El programa mostrará tu elección y la de la computadora, y declarará al ganador.
- Para salir del juego, escribe 'salir'.

¡Diviértete!
"""

import random
import sys

# Definimos la clase del juego
class PPT:
    def __init__(self):
        print('¡Bienvenido a Piedra, Papel o Tijeras 9000!')

        # Movimientos para mostrar con emojis
        self.movimientos: dict = {'piedra': '🪨', 'papel': '📜', 'tijeras': '✂️'}
        # Lista de movimientos válidos
        self.movimientos_validos: list[str] = list(self.movimientos.keys())

    # Método para jugar una ronda del juego
    def jugar(self):
        # Obtener la entrada del usuario y convertirla a minúsculas
        movimiento_usuario: str = input('¿Piedra, papel o tijeras? >> ').lower()

        # Dar al usuario la opción de salir
        if movimiento_usuario == 'salir':
            print('¡Gracias por jugar!')
            sys.exit()

        # Comprobar que el usuario hizo un movimiento válido, si no, intentar de nuevo
        if movimiento_usuario not in self.movimientos_validos:
            print('Movimiento inválido...')
            return self.jugar()

        # Movimiento de la IA (elige aleatoriamente)
        movimiento_ia: str = random.choice(self.movimientos_validos)

        self.mostrar_movimientos(movimiento_usuario, movimiento_ia)
        self.comprobar_movimiento(movimiento_usuario, movimiento_ia)

    # Método para mostrar los movimientos de ambos jugadores
    def mostrar_movimientos(self, movimiento_usuario: str, movimiento_ia: str):
        # Mostrar todo de manera agradable
        print('----')
        print(f'Tú: {self.movimientos[movimiento_usuario]}')
        print(f'IA: {self.movimientos[movimiento_ia]}')
        print('----')

    # Método para comprobar quién gana
    def comprobar_movimiento(self, movimiento_usuario: str, movimiento_ia: str):
        # Lógica del juego para determinar el ganador
        if movimiento_usuario == movimiento_ia:
            print('¡Es un empate!')
        elif movimiento_usuario == 'piedra' and movimiento_ia == 'tijeras':
            print('¡Tú ganas!')
        elif movimiento_usuario == 'tijeras' and movimiento_ia == 'papel':
            print('¡Tú ganas!')
        elif movimiento_usuario == 'papel' and movimiento_ia == 'piedra':
            print('¡Tú ganas!')
        else:
            print('La IA gana...')


# Punto de entrada del programa
if __name__ == '__main__':
    juego = PPT()

    while True:
        juego.jugar()
