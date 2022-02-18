from clases import Tablero, Barco
from variables import dimensiones

def crear_barcos():
    lista_esloras = [1,2,3,4]
    barcos = []
    for i in lista_esloras:
        cont = 0
        while cont < (5-i):
            barcos.append(Barco(i))
            cont = cont + 1
    return barcos


def play_hlf():
    
    barcos = crear_barcos()

    T_usuario_visible = Tablero('humano', dimensiones, 'visible')

    for barco in barcos:
        T_usuario_visible.iniciar_tablero()
        # T_usuario_visible.colocar_barcos(barco)