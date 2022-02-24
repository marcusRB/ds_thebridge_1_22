import os
import shutil

def recorrer_archivos(docs,imgs,softwares):
    for archivo in os.listdir():
        # archivo = archivo.lower()
        if not os.path.isdir(os.path.join(os.getcwd(),archivo)):
            print(archivo, ":es un archivo")
            if archivo.lower().endswith(docs):
                shutil.move(archivo,'documents')
            elif archivo.lower().endswith(imgs):
                shutil.move(archivo,'images')
            elif archivo.lower().endswith(softwares):
                shutil.move(archivo,'software')
            else:
                shutil.move(archivo,'others')
        else:
            print(archivo, ":es una carpeta")

def crear_directorios():
    os.makedirs('images', exist_ok = True)
    os.makedirs('documents', exist_ok = True)
    os.makedirs('software', exist_ok = True)
    os.makedirs('others', exist_ok = True)
