import random
import os

IMAGENES_AHORCADO = ['''

    +---+
    |   |
        |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========''']

#categorias = ['animales', 'colores']
animales = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()
colores = 'rojo verde azul blanco negro gris fucsia amarillo marron purpura'.split()

def obtenerPalabraAlAzar(listaDePalabras):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    índiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[índiceDePalabras]

def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):

    os.system ("cls")
    print("""
    *** A H O R C A D I T O ***
    tematica: """+ cate)
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacios = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): #completar los espacios vacios con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]

    for letra in espaciosVacios: #mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()

def obtenerIntento(letrasProbadas): #devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado solo una letra, y no otra cosa
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) !=1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra chivo')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('No podes con letras y queres sumar numeros?')
        else:
            return intento

def jugarDeNuevo():
    #esta funcion devuelve truew si el jugador quiere volver a jugar, en caso contrario devuelve False
    print('Queres jugar de nuevo? (si o no)')
    return input().startswith('s')

def pedirOpcion():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elegi un numero: "))
            correcto=True
        except ValueError:
            print('Elegi uno valido carnero!')
    return num

salir = False
opcion = 0

while not salir:
    os.system('cls')
    print("""
    Seleccione una categoria

    1 - Animales
    2 - Colores
    0 - vaycesese
    """)

    opcion = pedirOpcion()
    #global categoria
    
    if opcion==1:
        print("animales")
        cate = 'Animales'
        categoria = animales
        break
    elif opcion==2:
        print("colores")
        cate = "Colores"
        categoria = colores
        break
    elif opcion==0:
        print("vaycese")
        break
    else:
        print("Ideai")
        input("No has pulsado ninguna opcion correcta...\npor eso te hacen lo que te hacen")

letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(categoria)
juegoTerminado = False

while True:
    mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    #permite al jugador escribir una letra
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
        # Verifica si el jugador ha ganado
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            os.system('cls')
            print('***VICTORIA***\n\nBien chivo! la palabra secreta es "' + palabraSecreta + '"!\n\nhas ganao!')
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento

        # Comprobar si el jugador ha agotado sus intentos y ha perdido
        if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('*** Te has quedado sin intentos carnero!\nDespues de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"***')
            juegoTerminado = True

    #pregutar al jugador si quiere volver a jugar (pero solo si el juego ha terminado).
    if juegoTerminado:
        if jugarDeNuevo():
            pedirOpcion()
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(categoria)
        else:
            print('*** Gracias chivo! espero que la proxima ganes algo ***')
            break
