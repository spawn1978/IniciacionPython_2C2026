import funciones_sql
#from colorama import Fore, Back, Style, init
from colorama import Fore, init, Back, Style

init(autoreset=True)

# Solicita los datos de un producto y los guarda en la base de datos.
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

# Obtiene y muestra todos los productos registrados.
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

# Solicita un ID y muestra el producto que coincide.
def buscar_producto():
    while True:
        try:
            id = int(input(Fore.GREEN + "Ingrese el ID del producto que desea buscar: "))
            if id <= 0:
                print(Fore.RED + "El valor del ID debe ser un número positivo.")
                continue
            break
        
        except ValueError:
            print(Fore.RED + "El valor del ID no puede estar vacio y debe ser solo numeros positivos.")
            continue
    
    productos = funciones_sql.producto_buscado(id)
    if productos is None:
        return
    if not productos:
        print(Fore.RED + f"No se encontraron productos con ese ID '{id}'.")
        return
    
    print(Fore.GREEN + "\nRESULTADOS DE LA BÚSQUEDA")
    for id_encontrado, nombre, descripcion, categoria, cantidad, precio in productos:
        print(Fore.GREEN + f"ID: {id_encontrado} | Nombre: {nombre} | Descripcion: {descripcion} | Categoria: {categoria} | Cantidad: {cantidad} | Precio: ${precio}")

# Solicita un ID y elimina el producto correspondiente.
def eliminar_producto():    
    while True:
        try:
            id = int(input(Fore.GREEN + "Ingrese el ID del producto que desea eliminar: "))
                
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
    

