import os
archivo = "ususarios.txt"
archivo_ninja="ninja.txt"
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
            
#5. Actualizar contraseña
def actualizar_contraseña(datos): 
    correo = input("Ingrese el correo del usuario a actualizar: ")
    if correo not in datos:
        print("El correo no esta registrado o no existe, por favor ingresa uno valido: ")
        return
    nueva_contra = input("Ingrese una nueva contraseña (Minimo 6 caracteres): ")
    if len(nueva_contra) < 6:
        print("La contraseña ingresada es demasiado corta. Intente nuevamente: ")
        return
    datos [correo]["contrasena"] = nueva_contra
    print("Contraseña actualizada correctamente ")
    
#6. Eliminar usuario
def eliminar_usuario(datos): 
    correo = input("Ingrese el correo del usuario que se desea eliminar: ")
    if correo in datos:
        del datos[correo]
        print("El usuario ha sido eliminado correctamente: ")
    else: 
        print("El correo ingresado no existe o no esta registrado...")
        
#7. Loggear con los datos registrados USUARIO Y CONTRASEÑA

def login(datos): 
    correo = input("Ingrese el Correo: ")
    contrasena = input("Ingrese la Contraseña: ")
  
    if correo in datos and datos[correo]["contrasena"] == contrasena:
        print("ACCESO EXITOSO...")
        return True
        
    else:
        print("Correo o Contraseña Incorrectos ")
        return False
#8. MENU DEL SISTEMA

def menu():
    datos = cargar_datos()
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---\n")
        print("1. Registrar nuevo usuario")
        print("2. Leer usuarios")
        print("3. Actualizar contraseña")
        print("4. Eliminar usuario")
        print("5. Guardar cambios")
        print("6. Iniciar sesión")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            crear_usuario(datos)
        elif opcion == "2":
            leer_usuarios(datos)
        elif opcion == "3":
            actualizar_contraseña(datos)
        elif opcion == "4":
            eliminar_usuario(datos)
        elif opcion == "5":
            guardar_datos(datos)
        elif opcion == "6":
            login(datos)
            

        elif opcion == "7":
            confirmar = input("Seguro/a que desea salir?(Sus cambios no se guardaran): (s/n)").lower()
            if confirmar == "s": 
                print("Saliendo sin guardar...")
                break
            
            else: 
                print("Volviendo al menu...")
        else: 
            print("Opcion invalida... Por favor ingrese una del menu")

menu()
#crear archivo donde se va a guardar los datos de los ninjas creados.
def cargar_ninjas():
    if not os.path.exists(archivo_ninja):
        return{}
    with open(archivo_ninja, "r", encoding="uft-8") as file:
        lineas=file.readlines()
        datos_ninjas={}
        for linea in lineas:
            try:
                ninja=eval(linea.strip())
                nombre=ninja["nombre"]
                datos_ninjas[nombre]=ninja
            except:
                continue
        return datos_ninjas
#guardar datos de los ninjas creados en el archivo
def guardar_ninjas(datos_ninjas):
    with open(archivo_ninja, "w",encoding= "utf-8") as file:
        for ninja in datos_ninjas.values():
            file.write(str(ninja) + "\n")
        print("Los ninjas se han guardado correctamente")
#1Crear al ninja
def crear_ninja(datos_ninjas, habilidades_usadas):
    nombre=input("Nombre del ninja que deseas crear :").strip()
    if nombre in datos_ninjas:
        print("Ya existe un ninja con ese nombre")
        return
    habilidades=generar_habilidades(habilidades_usadas)
    ninja={"nombre":nombre,
           "fuerza":habilidades[0],
           "agilidad":habilidades[1],
           "resistencia":habilidades[2],
            }
    datos_ninjas[nombre]=ninja
    print(f"Ninja'{nombre}' creado con habilidades unicas.")
#generar habilidades sin que se repita para cada ninja.
def generar_habilidades(habilidades_usadas):
    habilidades=[]
    valor=30
    while len(habilidades)<3:
        if valor not in habilidades_usadas:
            habilidades.append(valor)
            habilidades_usadas.append(valor)
        valor+=30
        if valor>100:
            valor=20
    return habilidades
#2.leer ninja creado.
def leer_ninja(datos_ninjas):
    if not datos_ninjas:
        print("No hay ninjas registrados.")
    else:
        for ninja in datos_ninjas.values():
            print(f"Nombre: {ninja['nombre']} | Fuerza:{ninja['fuerza']} | Agilidaad: {ninja['agilidad']} | Resistencia: {ninja['resistencia']} ")
def actualizar_ninja(datos_ninjas,habilidades_usadas):
    nombre=input("Ingrese el nombre del ninja a actualizar:")
    if nombre not in datos_ninjas:
        print("Ninja no encontrado.")
        return
    habilidades=generar_habilidades(habilidades_usadas)
    datos_ninjas[nombre]={
         "fuerza":habilidades[0],
           "agilidad":habilidades[1],
           "resistencia":habilidades[2],
    }
    print(f"Ninja{'nombre'} actualizado con nuevas habilidades.")
#Eliminar ninjas
def eliminar_ninja(datos_ninjas):
    nombre=input("Ingrese el nombre del ninja que desea eliminar:")
    if nombre in datos_ninjas:
        del datos_ninjas[nombre]
        print("Ninja eliminado correctamente del sistema.")
    else:
        print('El ninja no existe.')
#Menu para entrar a la gestion de ninjas
def menu_ninjas():
    while True:
        print("\n----MENU DE NINJAS ----")
        print("1.Crear ninja")
        print("2.Leer ninjas")
        print("3.Actualizar ninjas")
        print("4.Eliminar ninjas")
        print("5.Guardar ninjas")
        print("6.Cerrar sesion")
        




