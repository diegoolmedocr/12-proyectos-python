"""
Este programa verifica si una contraseña se encuentra entre las 100,000 contraseñas más comunes.

Fuente: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt

Uso:
- Ejecuta el programa.
- Introduce una contraseña cuando se te solicite.
- El programa te informará si tu contraseña es común (y por lo tanto insegura) o si es única.

¡Utiliza este programa para mejorar la seguridad de tus contraseñas!
"""

# Función que verifica si una contraseña está en la lista de contraseñas comunes
def verificar_contraseña(contraseña: str):
    """
    Verifica si una contraseña está entre las 100,000 contraseñas más comunes.
    """

    # Abrimos el archivo que contiene las contraseñas más comunes
    with open('contraseñas.txt', 'r') as archivo:
        contraseñas_comunes: list[str] = archivo.read().splitlines()

    # Recorremos la lista de contraseñas comunes
    for i, contraseña_comun in enumerate(contraseñas_comunes, start=1):
        # Comparamos la contraseña del usuario con cada contraseña común
        if contraseña == contraseña_comun:
            # Si coinciden, informamos al usuario y salimos de la función
            print(f'{contraseña}: ❌ (#{i})')
            return  # Salimos de la función al encontrar una coincidencia

    # Si la contraseña no está en la lista, es única
    print(f'{contraseña}: ✅ (Única)')

# Función principal del programa
def main():
    # Solicitamos al usuario que introduzca una contraseña
    contraseña_usuario: str = input('Introduce una contraseña: ')
    # Llamamos a la función para verificar la contraseña
    verificar_contraseña(contraseña=contraseña_usuario)

# Ejecutamos la función principal si el script se ejecuta directamente
if __name__ == '__main__':
    main()
