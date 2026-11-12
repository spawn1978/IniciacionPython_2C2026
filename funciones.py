import funciones_sql
#from colorama import Fore, Back, Style, init
from colorama import Fore, init, Back, Style

init(autoreset=True)

# Funcion agregar_productos
def agregar_productos():
    
    # Ingresar el nombre del producto con validación
    nombre = input(Fore.WHITE + "Ingrese el nombre del producto: ").lower().strip()
    while nombre == "": 
        print(Fore.RED + "El nombre del producto no puede estar vacío y debe contener solo letras.")
        nombre = input(Fore.WHITE + "Ingrese el nombre del producto: ").lower().strip() 
        
    # Ingresar la descripción del producto con validación
    descripcion = input(Fore.WHITE + "Ingrese la descripción del producto: ").lower().strip()
    while descripcion == "": 
        print("La descripción del producto no puede estar vacía y debe contener solo letras.")
        descripcion = input("Ingrese la descripción del producto: ").lower().strip() 
        
                
    # Ingresar la categoría del producto con validación
    categoria = input(Fore.WHITE + "Ingrese la categoría del producto: ").lower().strip()
    while not categoria.isalpha():
        print(Fore.RED + "La categoría no puede estar vacía y debe contener solo letras.")
        categoria = input(Fore.WHITE + "Ingrese la categoría del producto: ").lower().strip()
    
    # Ingresar cantidad de productos con validación
    while True:
        try:
            cantidad = int(input(Fore.WHITE + "Ingrese la cantidad de productos: "))
            
            if cantidad <= 0:
                print(Fore.RED + "La cantidad de productos debe ser un número positivo.")
                continue  # Continuar solicitando la cantidad si es inválida
            else:
                break  # Salir del bucle si la cantidad es válida

        except ValueError:
            print(Fore.RED + "La cantidad de productos no puede estar vacía y debe ser solo numeros positivos.")
        
    # Ingresar el precio del producto con validación                    
    while True:
        try:
            precio = int(input(Fore.WHITE + "Ingrese el precio del producto: "))
            if precio <= 0:
                print(Fore.RED + "El precio debe ser un número positivo.")
                continue
            break  # Salir del bucle si la entrada es válido
        except ValueError:
            print(Fore.RED + "El valor del precio no puede estar vacío y debe ser solo numeros positivos.")    
                            
    funciones_sql.registrar_producto(nombre, descripcion, categoria, cantidad, precio)
    nombre = nombre.upper()             
    print(Fore.GREEN + f"Producto '{nombre}' agregado exitosamente.")
    #print(lista)  # Mostrar la lista de productos después de agregar uno nuevo

# Funcion mostrar_producto                    
def mostrar_productos():
    productos = funciones_sql.listar_producto()
    if productos is None:
        return
    if not productos:
        print(Fore.RED + "No hay productos registrados.")
        return

    print(Fore.LIGHTBLUE_EX + "\nLISTA DE PRODUCTOS")
    for id, nombre, descripcion, categoria, cantidad, precio in productos:
        print(Fore.LIGHTBLUE_EX + f"ID: {id} | Nombre: {nombre} | Descripcion: {descripcion} | Categoria: {categoria} | Cantidad: {cantidad} |  Precio: ${precio}")

# Funcion buscar_producto            
def buscar_producto():
    producto_buscado = input(Fore.GREEN + "Ingrese el nombre del producto que desea buscar: ").lower().strip()
    productos = funciones_sql.producto_buscado(producto_buscado)
    producto_buscado = producto_buscado.upper()
    
    if productos is None:
        return
    if not productos:
        print(Fore.RED + f"No se encontraron productos con el nombre '{producto_buscado}'.")
        return

    print(Fore.GREEN + "\nRESULTADOS DE LA BÚSQUEDA")
    for id_producto, nombre, descripcion, categoria, cantidad, precio in productos:
        print(Fore.GREEN + f"ID: {id_producto} | Nombre: {nombre} | Descripcion: {descripcion} | Categoria: {categoria} | Cantidad: {cantidad} | Precio: ${precio}")





###########################################
# Funcion actualizar_producto
# DESARROLLAR LA FUNCION!!!!!!!!!!!!!!!!!!
def actualizar_producto():
    producto_buscado = input(Fore.GREEN + "Ingrese el dato del producto(ID) que desea actualizar: ")
    
    productos = funciones_sql.producto_actualizado(producto_buscado)
    producto_buscado = producto_buscado.upper()

    if productos is None:
        return
    if not productos:
        print(Fore.RED + f"No se encontraron productos con el nombre '{producto_buscado}'.")
        return
    
    print(Fore.GREEN + "\nRESULTADOS DE LA BÚSQUEDA")
    for id_producto, nombre, descripcion, categoria, cantidad, precio in productos:
        print(Fore.GREEN + f"ID: {id_producto} | Nombre: {nombre} | Descripcion: {descripcion} | Categoria: {categoria} | Cantidad: {cantidad} | Precio: ${precio}")
###########################################

# Funcion eliminar_producto
def eliminar_producto():    
    while True:
        try:
            id = int(input(Fore.WHITE + "Ingrese el ID del producto que desea eliminar: "))
                
            if id <= 0:
                print(Fore.RED + "El valor del ID debe ser un número positivo.")
                continue  # Continuar solicitando la cantidad si es inválida
            else:
                break  # Salir del bucle si la cantidad es válida
    
        except ValueError:
            print(Fore.RED + "El valor del ID no puede estar vacio y debe ser solo numeros positivos.")
        return
                
    producto = funciones_sql.producto_eliminado(id)
    if producto is None:
        print(Fore.RED + f"No se encontraron productos con ese ID '{id}'.")
        return

    print(Fore.GREEN + f"Producto '{producto}' con ID '{id}' eliminado exitosamente.")
