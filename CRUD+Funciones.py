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
def guardar_datos(datos):
    with open(archivo, "w", encoding="utf-8") as file:
        for usuario in datos.values():
            file.write(str(usuario) + "\n")
    print("Los datos se han guardado correctamente")
    
#3. Crear ususario - Registros
def crear_usuario(datos):
    correo = input("Ingrese el correo: ")
    if correo in datos: 
        print("El correo ingresado ya se encuentra registrado, por favor ingrese uno diferente:  ")
    if "@" not in correo or "." not in correo:
        print("Correo no valido")
        return
    contrasena = input("Ingrese una contraseña (minimo 6 caracteres): ")
    if len(contrasena) < 6: 
       print("Contraseña muy corta por favor ingrese otra: ")
       return
    usuario= {"correo": correo, "contraseña": contrasena}
    datos[correo] = usuario 
    print("Usuario registrado correctamente...")
    
   
#4. Leer ususarios registrados 
def leer_usuarios(datos): 
    if not datos: 
        print("No existen usuarios registrados...")
    else: 
        for usuario in datos.values():
            print(f"correo: {usuario['correo']} | Contraseña: {usuario['contrasena']}")
            
        
        
        

        