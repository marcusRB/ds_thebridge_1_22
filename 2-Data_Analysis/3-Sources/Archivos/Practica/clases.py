import os
import shutil

class Tipo:

    def __init__(self, folder, extension):
        self.folder = folder
        self.extension = extension
        self.crear_directorios()
        self.recorrer_archivos()
    
    def crear_directorios(self):
        os.makedirs(self.folder, exist_ok = True)

    def recorrer_archivos(self):
        for archivo in os.listdir(os.getcwd()):
            if not os.path.isdir(os.path.join(os.getcwd(),archivo)):
                if archivo.lower().endswith(self.extension) or self.extension==():
                    shutil.move(archivo, self.folder)