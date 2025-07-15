import os
archivo = "ususarios.txt"

#1. Cargar los datos del archivo 

def cargar_datos():
    if not os.path.exists(archivo): 
        return {}
    with open(archivo, "r", encoding="utf-8") as file:
        lineas = file.readlines()
        datos = {}
        for linea in lineas: 
            try: 
                usuario = eval(linea.strip())
                correo = usuario["correo"]
                datos[correo] = usuario
            except: 
                continue
        return datos
    
#2. Apartado para guardar datos en el archivo creado... 