


lista_productos = [
    ["manazana", "fruta", 1000],
    ["pera", "fruta", 2000],
    ["banana", "fruta", 1500]
]    

while True:
    print("Sistema de Gestión de Productos".upper())
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ".strip())  

    match opcion:
        case "1":

        case "2":

        case "3":

        case "4":

        case "5": 
            print("Saliendo del sistema...")
            break
        case _: # Case default   
            print("Opción no válida. Por favor, seleccione una opción válida.")