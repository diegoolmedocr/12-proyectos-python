"""
Este programa es un sencillo juego del "Ahorcado" en el que el usuario debe adivinar una palabra letra por letra.

Se han agregado más de 50 palabras comunes para aumentar la diversión y el desafío del juego.

Uso:
- Ejecuta el programa.
- Introduce tu nombre cuando se te solicite.
- Adivina la palabra ingresando una letra en cada turno.
- Tienes un número limitado de intentos. ¡Buena suerte!

¡Diviértete!
"""

from random import choice

# Función principal del juego
def ejecutar_juego():
    # Lista ampliada de palabras comunes para el juego
    palabras = [
        'manzana', 'secreto', 'banana', 'casa', 'perro', 'gato', 'mesa', 'silla', 'ventana',
        'puerta', 'libro', 'escuela', 'coche', 'avion', 'computadora', 'telefono', 'amigo',
        'familia', 'comida', 'bebida', 'agua', 'trabajo', 'dinero', 'salud', 'musica',
        'pelicula', 'deporte', 'playa', 'montaña', 'ciudad', 'pais', 'mundo', 'sol', 'luna',
        'estrella', 'cielo', 'mar', 'rio', 'bosque', 'flor', 'arbol', 'corazon', 'amor',
        'vida', 'tiempo', 'dia', 'noche', 'año', 'mes', 'semana', 'hora', 'minuto', 'segundo',
        'felicidad', 'sonrisa', 'amabilidad', 'paz', 'esperanza', 'libertad', 'justicia',
        'honestidad', 'valentia', 'respeto', 'tolerancia', 'paciencia', 'sabiduria',
        'energia', 'fuerza', 'creatividad', 'imaginacion', 'aventura', 'descubrimiento',
        'naturaleza', 'historia', 'cultura', 'educacion', 'arte', 'ciencia', 'tecnologia',
        'literatura', 'filosofia', 'matematicas', 'fisica', 'quimica', 'biologia',
        'geografia', 'economia', 'politica', 'sociedad', 'religion', 'tradicion',
        'comunidad', 'comunicacion', 'informacion', 'internet', 'programacion', 'codigo'
    ]

    # Seleccionamos una palabra aleatoria de la lista ampliada
    palabra: str = choice(palabras)

    # Un mensaje de bienvenida interactivo y amistoso
    nombre_usuario: str = input('¿Cómo te llamas? >> ')
    print(f'¡Bienvenido al juego del ahorcado, {nombre_usuario}!')

    # Configuración inicial
    adivinadas: str = ''  # Contendrá todas las letras que se han adivinado
    intentos: int = 6     # Establece la cantidad de intentos que tendrá el usuario

    # El juego comienza aquí
    while intentos > 0:
        espacios: int = 0

        print('Palabra: ', end='')
        # Recorremos cada carácter de la palabra
        for caracter in palabra:
            if caracter in adivinadas:
                # Si la letra ha sido adivinada, la mostramos
                print(caracter, end=' ')
            else:
                # Si no, mostramos un guión bajo
                print('_', end=' ')
                espacios += 1

        print()  # Añade una línea en blanco

        # Si no quedan espacios, significa que el usuario ha ganado
        if espacios == 0:
            print('¡Felicidades, has adivinado la palabra!')
            break

        # Obtener la entrada del usuario
        adivinanza: str = input('Introduce una letra: ').lower()

        # Validar que el usuario introduzca solo una letra
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print('Por favor, introduce una sola letra.')
            continue

        # Comprobar que el usuario no repita la misma letra
        if adivinanza in adivinadas:
            print(f'Ya has usado la letra "{adivinanza}". ¡Intenta con otra!')
            continue

        # Añadir la adivinanza a las letras usadas
        adivinadas += adivinanza

        # Comprobar si la letra adivinada está en la palabra
        if adivinanza not in palabra:
            intentos -= 1
            print(f'La letra "{adivinanza}" no está en la palabra. Te quedan {intentos} intentos.')

            # Fin del juego si los intentos llegan a 0
            if intentos == 0:
                print('No te quedan más intentos... Has perdido.')
                print(f'La palabra era: "{palabra}".')
                break
        else:
            print(f'¡Bien hecho! La letra "{adivinanza}" está en la palabra.')

# Ejecutamos la función principal si el script se ejecuta directamente
if __name__ == '__main__':
    ejecutar_juego()
