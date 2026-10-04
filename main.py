


lista_productos = [
    ["manazana", "fruta", 1000],
    ["pera", "fruta", 2000],
    ["banana", "fruta", 1500]
]    

while True:
    print("===================================")
    print("| Sistema de Gestión de Productos |".upper())
    print("===================================")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ".strip())  

    match opcion:
        case "1": # Agregar producto
            nombre = input("Ingrese el nombre del producto: ").lower().strip()
            while nombre == "": 
                print("El nombre del producto no puede estar vacío y debe contener solo letras.")
                nombre = input("Ingrese el nombre del producto: ").lower().strip() 

            categoria = input("Ingrese la categoría del producto: ").lower().strip()
            while categoria == "": 
                print("El nombre de la categoria no puede estar vacío y debe contener solo letras.")
                categoria = input("Ingrese la categoria del producto: ").lower().strip() 

            precio = (input("Ingrese el precio del producto: "))
            while not precio.isdigit():
                print("El valor del precio no puede estar vacío y debe ser solo numeros positivos.")
                precio = input("Ingrese el precio del producto: ")

            precio = int(precio)  # Convertir el precio a entero después de la validación

            producto = [nombre, categoria, precio]  
            lista_productos.append(producto)

            print(f"Producto '{nombre}' agregado exitosamente.")
            print(lista_productos)  # Mostrar la lista de productos después de agregar uno nuevo


        # case "2":

        # case "3":

        case "4":
            for i in range(len(lista_productos)):
                print(f"{i + 1}. {lista_productos[i][0].capitalize()} - {lista_productos[i][1].capitalize()} - ${lista_productos[i][2]}")

                numero_producto = input("Ingrese el número del producto que desea eliminar: ")
                while not numero_producto.isdigit() or int(numero_producto) < 1 or int(numero_producto) > len(lista_productos):
                    print("Número de producto inválido. Por favor, ingrese un número válido.")
                    numero_producto = input("Ingrese el número del producto que desea eliminar: ")

                producto_eliminado = lista_productos.pop(int(numero_producto) - 1)
                print(f"Producto '{producto_eliminado[0]}' eliminado exitosamente.")

        case "5": 
            print("Saliendo del sistema...")
            break
        case _: # Case default   
            print("Opción no válida. Por favor, seleccione una opción válida.")