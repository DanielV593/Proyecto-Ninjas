import os
import random
import json
import re

archivo = "usuarios.txt"
archivo_ninja="ninja.txt"
archivo_habilidades = "habilidades_ninja.txt"
archivo_grafo = "grafo_ninjas.json"

#Arbol Binario de Habilidades

arbol = {
    'valor':'fuerza',
    'izquierda':{
        'valor':'agilidad',
        'izquierda':{'valor':'destreza','izquierda':None,'derecha':None},
        'derecha':None
    },
        'derecha':{
        'valor':'resistencia',
        'izquierda':None,
        'derecha':{'valor':'velocidad','izquierda':None, 'derecha':None}
    }
}

def inOrder(nodo,Recorrido):
    if nodo is not None:
        inOrder(nodo['izquierda'], Recorrido)
        Recorrido.append(nodo['valor'])
        inOrder(nodo['derecha'],Recorrido)

def preOrder(nodo, Recorrido):
    if nodo is not None:
        Recorrido.append(nodo['valor'])       
        preOrder(nodo['izquierda'], Recorrido)
        preOrder(nodo['derecha'], Recorrido)

def postOrder(nodo, Recorrido):
    if nodo is not None:
        postOrder(nodo['izquierda'], Recorrido)
        postOrder(nodo['derecha'], Recorrido)
        Recorrido.append(nodo['valor'])

def mostrarRecorridos():
    in_orden, pre_orden, post_orden = [], [], []
    inOrder(arbol, in_orden)
    preOrder(arbol, pre_orden)
    postOrder(arbol, post_orden)

    print("\n--- RECORRIDOS DEL ÁRBOL DE HABILIDADES ---")
    print("InOrder:", in_orden)
    print("PreOrder:", pre_orden)
    print("PostOrder:", post_orden)

#Validaciones
def validar_correo(correo):  
    return "@" in correo and "." in correo and correo.strip() != ""

def validar_contrasena(contra):  
    return len(contra) >= 6

def validar_nombre_ninja(nombre):  
    return nombre.isalpha() and len(nombre) > 0
def validar_nombre_usuario(nombre):
    import re
    if not isinstance(nombre, str):
        return False
    nombre = nombre.strip()
    patron = r'^[A-Za-z0-9 @._-]+$'
    return bool(re.match(patron, nombre)) and len(nombre) > 0

#Cargar los datos del archivo 

def cargar_datos():
    if not os.path.exists(archivo): 
        open(archivo, "w", encoding="utf-8").close()
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
def guardar_datos(datos):
    with open(archivo, "w", encoding="utf-8") as file:
        for correo, usuario in datos.items():
            usuario["correo"] = correo  
            file.write(str(usuario) + "\n")
    print("Los datos se han guardado correctamente")
# Crear usuario - Registros
def crear_usuario(datos):
    correo = input("Ingrese el correo: ")

    if correo in datos:
        print(" El correo ingresado ya está registrado. Intente con uno diferente.")
        return
    if not validar_correo(correo):
        print(" Correo no válido. Intente nuevamente.")
        return
    contrasena = input("Ingrese una contraseña (mínimo 6 caracteres): ")
    if not validar_contrasena(contrasena):
        print(" Contraseña muy corta, ingrese otra.")
        return
    nombre_usuario = input("Ingrese su nombre (puede incluir letras, números y caracteres especiales): ")
    if not validar_nombre_usuario(nombre_usuario):
        print(" Nombre inválido, solo se permiten letras, números y caracteres especiales.")
        return
    datos[correo] = {
        "correo": correo,
        "nombre": nombre_usuario,
        "contrasena": contrasena
    }

    print(f" Usuario '{nombre_usuario}' creado exitosamente con el correo {correo} ")
# Leer ususarios registrados 
def leer_usuarios(datos):  
    if not datos: 
        print("No existen usuarios registrados...")
    else: 
        for usuario in datos.values():
            print(f"Correo: {usuario['correo']} | Contraseña: {usuario['contrasena']}")
# Actualizar contraseña
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

# Eliminar usuario
def eliminar_usuario(datos): 
    correo = input("Ingrese el correo del usuario que se desea eliminar: ")
    if correo in datos:
        del datos[correo]
        print("El usuario ha sido eliminado correctamente: ")
    else: 
        print("El correo ingresado no existe o no esta registrado...") 
# Loggear con los datos registrados USUARIO Y CONTRASEÑA

def login(datos): 
    correo = input("Ingrese el Correo: ")
    contrasena = input("Ingrese la Contraseña: ")
  
    if correo in datos and datos[correo]["contrasena"] == contrasena:
        print("ACCESO EXITOSO...")
        return True     
    else:
        print("Correo o Contraseña Incorrectos ")
        return False   

def generar_habilidades():
    habilidades = []
    inOrder(arbol, habilidades)
    return {h: random.randint(10, 100) for h in habilidades}

#Silumacion de combate

def combate_1vs1(datos_ninjas):
    if len(datos_ninjas) < 2:
        print("Se necesitan al menos 2 ninjas para combatir")
        return

    print("\nNinjas disponibles:")
    for nombre in datos_ninjas:
        print("-", nombre)

    nombre1 = input("Primer ninja: ")
    nombre2 = input("Segundo ninja: ")

    if nombre1 not in datos_ninjas or nombre2 not in datos_ninjas:
        print("Uno o ambos ninjas no existen")
        return

    n1, n2 = datos_ninjas[nombre1], datos_ninjas[nombre2]
    total1 = n1["fuerza"] + n1["agilidad"] + n1["resistencia"]
    total2 = n2["fuerza"] + n2["agilidad"] + n2["resistencia"]

    print(f"\n--- COMBATE ENTRE {nombre1} VS {nombre2} ---")
    print(f"{nombre1}: Fuerza={n1['fuerza']}, Agilidad={n1['agilidad']}, Resistencia={n1['resistencia']} (Total: {total1})")
    print(f"{nombre2}: Fuerza={n2['fuerza']}, Agilidad={n2['agilidad']}, Resistencia={n2['resistencia']} (Total: {total2})")

    if total1 > total2:
        ganador = nombre1
    elif total2 > total1:
        ganador = nombre2
    else:
        ganador = "Empate"

    print("\n--- RESULTADO ---")
    print(f"Ganador: {ganador}")

    with open(archivo_habilidades, "a", encoding="utf-8") as f:
        f.write(f"\nCombate entre {nombre1} y {nombre2}\n")
        f.write(f"{nombre1}: {n1}\n")
        f.write(f"{nombre2}: {n2}\n")
        f.write(f"Ganador: {ganador}\n")
   
# Cargar ninjas
def cargar_ninjas():
    if not os.path.exists(archivo_ninja):
        open(archivo_ninja, "w", encoding="utf-8").close()
        return {}
    with open(archivo_ninja, "r", encoding="utf-8") as file:
        lineas = file.readlines()
        datos_ninjas = {}
        for linea in lineas:
            try:
                ninja = json.loads(linea.strip())
                nombre = ninja["nombre"]
                datos_ninjas[nombre] = ninja
            except json.JSONDecodeError:
                continue
        return datos_ninjas
    
#guardar datos de los ninjas creados en el archivo

def guardar_ninjas(datos_ninjas):
    with open(archivo_ninja, "w",encoding= "utf-8") as file:
        for ninja in datos_ninjas.values():
            file.write(json.dumps(ninja) + "\n")
        print("Los ninjas se han guardado correctamente")

#Crear al ninja

def crear_ninja(datos_ninjas, habilidades_usadas):  # <--- dos argumentos
    nombre = input("Nombre del ninja que deseas crear: ").strip()
    if nombre in datos_ninjas:
        print("Ya existe un ninja con ese nombre")
        return
    habilidades = generar_habilidades(habilidades_usadas)
    ninja = {
        "nombre": nombre,
        "fuerza": habilidades[0],
        "agilidad": habilidades[1],
        "resistencia": habilidades[2],
    }
    datos_ninjas[nombre] = ninja
    print(f"Ninja '{nombre}' creado con habilidades únicas.")



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

# leer ninja creado.
def leer_ninja(datos_ninjas):
    if not datos_ninjas:
        print("No hay ninjas registrados.")
    else:
        for ninja in datos_ninjas.values():
            print(f"Nombre: {ninja['nombre']} | Fuerza:{ninja['fuerza']} | Agilidaad: {ninja['agilidad']} | Resistencia: {ninja['resistencia']} ")
def eliminar_ninja(datos_ninjas):
    nombre = input("Ingrese el nombre del ninja a eliminar: ")
    if nombre in datos_ninjas:
        del datos_ninjas[nombre]
        print("Ninja eliminado correctamente del sistema.")
    else:
        print('El ninja no existe.')
        

def cargar_grafo():  
    if os.path.exists(archivo_grafo):
        with open(archivo_grafo, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_grafo(grafo): 
    with open(archivo_grafo, "w", encoding="utf-8") as f:
        json.dump(grafo, f)
    print("Grafo guardado correctamente.")

def agregar_conexion(grafo, origen, destino):
    if origen not in grafo:
        grafo[origen] = []
    if destino not in grafo:
        grafo[destino] = []
    grafo[origen].append(destino)
    grafo[destino].append(origen)
    print(f"Conexión creada entre {origen} y {destino}.")

def mostrar_conexiones(grafo):
    if not grafo:
        print("No hay conexiones entre ninjas aún.")
        return
    print("\n--- GRAFO DE NINJAS ---")
    for ninja, conexiones in grafo.items():
        print(f"{ninja} -> {', '.join(conexiones)}")

def buscar_conexion(grafo, origen, destino, visitados=None):
    if visitados is None:
        visitados = set()
    if origen not in grafo:
        return False
    if origen == destino:
        return True
    visitados.add(origen)
    for vecino in grafo[origen]:
        if vecino not in visitados and buscar_conexion(grafo, vecino, destino, visitados):
            return True
    return False


#8. MENU DEL SISTEMA

def menu_ninjas():
    datos_ninjas = cargar_ninjas()
    grafo_ninjas = cargar_grafo() 
    habilidades_usadas = []
    while True:
        print("\n----MENU DE NINJAS ----")
        print("1.Crear ninja")
        print("2.Leer ninjas")
        print("3. Crear conexion entre ninjas (Grafo)")
        print("4.Eliminar ninjas")
        print("5.Guardar ninjas y grafo")
        print("6. Combatir 1vs1 entre ninjas")
        print("7. Cerrar sesion")
        print("8. Mostrar recorridos en el arbol")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            crear_ninja(datos_ninjas, habilidades_usadas)
        elif opcion == "2":
            leer_ninja(datos_ninjas)
        elif opcion == "3":
            n1 = input("Primer ninja: ")
            n2 = input("Segundo ninja: ")
            if n1 in datos_ninjas and n2 in datos_ninjas:
                agregar_conexion(grafo_ninjas, n1, n2)
            else:
                print("Uno o ambos ninjas no existen.")
        elif opcion == "4":
            eliminar_ninja(datos_ninjas)  
        elif opcion == "5":
            guardar_ninjas(datos_ninjas)
            guardar_grafo(grafo_ninjas)
        elif opcion == "7":
            print("Cerrando sesión de ninjas.")
            break
        elif opcion == "6":
            combate_1vs1(datos_ninjas)  
        elif opcion == "8":
            mostrarRecorridos()
        else:
            print("Opción inválida.")

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
           if  login(datos):
                menu_ninjas()
                print("Regresando al menu de usuarios.")
        elif opcion == "7":
            confirmar = input("Seguro/a que desea salir?(Sus cambios no se guardaran): (s/n)").lower()
            if confirmar == "s": 
                print("Saliendo sin guardar...")
                break
            
            else: 
                print("Volviendo al menu...")
        else: 
            print("Opcion invalida... Por favor ingrese una del menu")

#Menu para entrar a la gestion de ninjas

menu()