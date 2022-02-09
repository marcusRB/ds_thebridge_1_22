import time
from otro.otras_funciones import hide_characters

def play_ahorcado(palabra, vidas):

    lista_oculta = hide_characters(palabra)

    # Inicializamos fallos
    fallos = 0

    while fallos < vidas: # Mientras nos queden fallos seguimos en el juego
        time.sleep(1)
        letra_usuario = input("Introduzca una letra").upper()  # Introduce el usuario la letra
        # Comprobamos si la letra se encuentra, buscamos en qué posicion se encuentra, y aquellos que coincidan, sustituiremos el valor de esa letra en su posicion
        if letra_usuario in palabra:
            for pos, letra in enumerate(palabra):
                if letra == letra_usuario:
                    lista_oculta[pos] = letra_usuario
        # Actualizamos la variable fallos, si llegamos a 6 se parará el bucle y mostrará por pantalla game over
        else: 
            fallos = fallos + 1
            print("Has fallado, llevas " + str(fallos) + ' fallos')
            if fallos == vidas:
                print("Game over")
        # En cada letra se muestra la palabra oculta con las letras acertadas
        print(' '.join(lista_oculta))

        # Si no encuentra letras por adivinar, has ganado
        if '_' not in lista_oculta:
            print("Well done")
            break