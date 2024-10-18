"""
Este programa es un juego sencillo de 'Historias Locas' (Mad Libs) en el que el usuario ingresa diferentes tipos de palabras (sustantivos, adjetivos, verbos) y se genera una historia divertida con esas palabras.

Ahora, el programa también te preguntará por el género de los sustantivos para usar los artículos y preposiciones correctos en la historia.

Uso:
- Ejecuta el programa.
- Ingresa las palabras solicitadas cuando se te pidan, incluyendo el género de los sustantivos.
- Disfruta de la historia personalizada que se genera al final.

¡Diviértete!
"""

# Función para obtener un sustantivo y su género
def obtener_sustantivo():
    # Solicitamos al usuario que introduzca un sustantivo
    sustantivo = input("Introduce un sustantivo: ")
    # Solicitamos al usuario que indique el género del sustantivo
    genero = input("¿El sustantivo es masculino o femenino? (m/f): ")
    return sustantivo, genero

# Función para obtener otros tipos de palabras (adjetivos, verbos, etc.)
def obtener_entrada(tipo_palabra: str):
    # Solicitamos al usuario que introduzca una palabra del tipo especificado
    entrada_usuario: str = input(f"Introduce un(a) {tipo_palabra}: ")
    return entrada_usuario

# Función para obtener el artículo indefinido correcto según el género
def articulo_indefinido(genero):
    return "un" if genero == 'm' else "una"

# Función para obtener el artículo definido correcto según el género
def articulo_definido(genero):
    return "el" if genero == 'm' else "la"

# Función para obtener la preposición 'a' con el artículo correcto según el género
def preposicion_a_articulo(genero):
    return "al" if genero == 'm' else "a la"

# Función para convertir un verbo en gerundio
def gerundio(verbo: str) -> str:
    if verbo.endswith("ar"):
        return verbo[:-2] + "ando"
    elif verbo.endswith("er") or verbo.endswith("ir"):
        return verbo[:-2] + "iendo"
    else:
        # Si no se puede procesar, se devuelve el verbo tal cual
        return verbo

# Obtenemos las palabras del usuario
sustantivo1, genero1 = obtener_sustantivo()
adjetivo1 = obtener_entrada("adjetivo")
verbo1 = obtener_entrada("verbo")
sustantivo2, genero2 = obtener_sustantivo()
verbo2 = obtener_entrada("verbo")

# Creamos la historia utilizando las palabras ingresadas y los artículos correctos
historia = f"""
Había una vez {articulo_indefinido(genero1)} {adjetivo1} {sustantivo1} que le encantaba {verbo1} todo el día.

Un día, {sustantivo2} entró en la habitación y sorprendió {preposicion_a_articulo(genero1)} {sustantivo1} en el acto.

{sustantivo2}: "¿Qué estás haciendo?"
{sustantivo1}: "Solo estoy {gerundio(verbo1)}, ¿cuál es el problema?"
{sustantivo2}: "Bueno, no todos los días ves a {articulo_indefinido(genero1)} {sustantivo1} {gerundio(verbo1)} en medio del día."
{sustantivo1}: "Supongo que tienes razón. Tal vez debería tomar un descanso."
{sustantivo2}: "Probablemente sea una buena idea. ¿Por qué no vamos a {verbo2} en su lugar?"
{sustantivo1}: "¡Claro, suena divertido!"

Y así, {sustantivo2} y {articulo_definido(genero1)} {sustantivo1} se fueron a {verbo2} y se lo pasaron genial.
Fin.
"""

# Imprimimos la historia final en pantalla
print(historia)
