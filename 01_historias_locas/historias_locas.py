"""
Este programa es un juego sencillo de 'Historias Locas' (Mad Libs) en el que el usuario ingresa diferentes tipos de palabras (sustantivos, adjetivos, verbos) y se genera una historia divertida con esas palabras.

Ahora, el programa también te preguntará por el género de los sustantivos para usar los artículos correctos en la historia.

Uso:
- Ejecuta el programa.
- Ingresa las palabras solicitadas cuando se te pidan, incluyendo el género de los sustantivos.
- Disfruta de la historia personalizada que se genera al final.

¡Diviértete!
"""

# Definimos una función para obtener la entrada del usuario
def obtener_entrada(tipo_palabra: str):
    # Solicitamos al usuario que ingrese una palabra del tipo especificado
    entrada_usuario: str = input(f"Ingresa un(a) {tipo_palabra}: ")
    return entrada_usuario

# Definimos una función específica para obtener un sustantivo y su género
def obtener_sustantivo():
    # Solicitamos al usuario que ingrese un sustantivo
    sustantivo = input("Ingresa un sustantivo: ")
    # Solicitamos el género del sustantivo
    while True:
        genero = input("¿Es masculino o femenino? (m/f): ").lower()
        if genero in ('m', 'f'):
            break
        else:
            print("Por favor, ingresa 'm' para masculino o 'f' para femenino.")
    # Retornamos el sustantivo y su género
    return sustantivo, genero

# Funciones para obtener los artículos correctos según el género
def articulo_definido(genero):
    # Retorna 'el' o 'la' según el género
    return 'el' if genero == 'm' else 'la'

def articulo_indefinido(genero):
    # Retorna 'un' o 'una' según el género
    return 'un' if genero == 'm' else 'una'

def preposicion_a_articulo(genero):
    # Retorna 'al' o 'a la' según el género
    return 'al' if genero == 'm' else 'a la'

def preposicion_a_articulo_indefinido(genero):
    # Retorna 'a un' o 'a una' según el género
    return 'a un' if genero == 'm' else 'a una'

# Obtenemos las palabras del usuario
sustantivo1, genero1 = obtener_sustantivo()
adjetivo1 = obtener_entrada("adjetivo")
verbo1 = obtener_entrada("verbo")
sustantivo2, genero2 = obtener_sustantivo()
verbo2 = obtener_entrada("verbo")

# Creamos la historia utilizando las palabras ingresadas y los artículos correctos
historia = f"""
Había una vez {articulo_indefinido(genero1)} {sustantivo1} {adjetivo1} que le encantaba {verbo1} todo el día.

Un día, {sustantivo2} entró en la habitación y sorprendió {preposicion_a_articulo(genero1)} {sustantivo1} en el acto.

{sustantivo2}: "¿Qué estás haciendo?"
{sustantivo1}: "Solo estoy {verbo1}ando, ¿cuál es el problema?"
{sustantivo2}: "Bueno, no es todos los días que ves {preposicion_a_articulo_indefinido(genero1)} {sustantivo1} {verbo1}ando en medio del día."
{sustantivo1}: "Supongo que tienes razón. Quizás debería tomar un descanso."
{sustantivo2}: "Probablemente sea una buena idea. ¿Por qué no vamos a {verbo2} en su lugar?"
{sustantivo1}: "¡Claro, suena divertido!"

Y así, {sustantivo2} y {articulo_definido(genero1)} {sustantivo1} se fueron a {verbo2} y pasaron un gran momento.
Fin.
"""

# Imprimimos la historia final en pantalla
print(historia)