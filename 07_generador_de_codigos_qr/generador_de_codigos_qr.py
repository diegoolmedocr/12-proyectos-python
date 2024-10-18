"""
Este programa simplifica la creación de códigos QR mediante una clase personalizada.

Uso:
- Ejecuta el programa.
- Introduce el texto que deseas convertir en un código QR cuando se te solicite.
- El programa generará un código QR con las especificaciones dadas y lo guardará en un archivo de imagen.

Nota:
- Asegúrate de tener instalados los módulos 'qrcode' y 'Pillow' (puedes instalarlos usando 'pip install qrcode[pil]').

¡Disfruta creando tus propios códigos QR!
"""

import qrcode  # Recuerda instalar Pillow para los colores (pip install qrcode[pil])

# Definimos la clase MiQR
class MiQR:
    """Una clase que simplifica la creación de códigos QR"""

    def __init__(self, tamaño: int, relleno: int):
        # Inicializamos la instancia de QRCode con el tamaño y el relleno proporcionados
        self.qr = qrcode.QRCode(box_size=tamaño, border=relleno)

    def crear_qr(self, nombre_archivo: str, fg: str, bg: str):
        """
        Crea un código QR con alguna personalización del usuario.

        :param nombre_archivo: El nombre o ruta de tu código QR.
        :param fg: El color de primer plano.
        :param bg: El color de fondo.
        :return: None
        """

        # Obtener la entrada del usuario
        entrada_usuario: str = input('Introduce el texto para el código QR: ')

        try:
            # Añadir la entrada del usuario al código QR y crearlo
            self.qr.add_data(entrada_usuario)
            qr_imagen = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_imagen.save(nombre_archivo)

            # Mostrar que se creó exitosamente
            print(f'¡Creado exitosamente! ({nombre_archivo})')
        except Exception as e:
            # Manejo de excepciones en caso de error
            print(f'Error: {e}')

# Función principal del programa
def main():
    # Creamos una instancia de MiQR con tamaño y relleno especificados
    miqr = MiQR(tamaño=10, relleno=4)
    # Llamamos al método crear_qr con el nombre del archivo y los colores de primer plano y fondo
    miqr.crear_qr(nombre_archivo='codigo_qr.png',
                  fg='#48c9b0',
                  bg='white')

# Ejecutamos la función principal si el script se ejecuta directamente
if __name__ == '__main__':
    main()
