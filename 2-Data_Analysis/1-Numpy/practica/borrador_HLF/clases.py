import numpy as np

class Barco:
    
    def __init__(self, eslora):
        self.eslora = eslora   

class Tablero:

    def __init__(self, id, dimensiones, tipo):
        self.id = id
        self.dimensiones = dimensiones
        self.tipo = tipo
    
    def iniciar_tablero(self):
        return print(np.full(self.dimensiones, fill_value = ' '))
    
    def colocar_barcos(self, barco):
        np.full(self.dimensiones, fill_value = ' ')
        fila = np.random.randint(0,10)
        columna = np.random.randint(0,10)
        ...
        return...