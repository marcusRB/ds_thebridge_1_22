import os
# from funciones import recorrer_archivos, crear_directorios
from variables import doc_types, img_types, software_types, carpeta, notebooks_types
from clases import Tipo

os.chdir(os.path.dirname(__file__)) # Cambia el path al de este propio archivo
os.chdir(os.path.join(os.getcwd(), carpeta)) # Cambia el path al de la carpeta del ejericio

docs = Tipo('documents', doc_types)
imgs = Tipo('images', img_types)
softs = Tipo('software', software_types)
others = Tipo('others', ())
notebooks = Tipo('notebooks', notebooks_types)
