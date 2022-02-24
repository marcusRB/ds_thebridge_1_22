import os
import shutil
# print(os.getcwd())
os.chdir('C:/Users/Miguel Angel/Documents/Bootcamp_DS_1_22/ds_thebridge_1_22/2-Data_Analysis/3-Sources/Archivos/Practica/directorio_prueba')

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg')

os.makedirs('images', exist_ok = True)
os.makedirs('documents', exist_ok = True)
os.makedirs('software', exist_ok = True)
os.makedirs('others', exist_ok = True)


for archivo in os.listdir():
    # archivo = archivo.lower()
    if not os.path.isdir(os.path.join(os.getcwd(),archivo)):
        print(archivo, ":es un archivo")
        if archivo.lower().endswith(doc_types):
            shutil.move(archivo,'documents')
        elif archivo.lower().endswith(img_types):
            shutil.move(archivo,'images')
        elif archivo.lower().endswith(software_types):
            shutil.move(archivo,'software')
        else:
            shutil.move(archivo,'others')
    else:
        print(archivo, ":es una carpeta")