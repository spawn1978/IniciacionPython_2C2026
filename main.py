#!/usr/bin/env python3
# Sistema de Gestión de Productos

"""
Nombre del Módulo: main.py
Descripción: Este script agrega productos, visualiza productos, busca productos y elimina productos de una lista.
Autor: Carlos Leguizmaon
Fecha de Creación: 2026-10-04
Versión: 1.0.0
"""



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

        case "2":
            print("======================")    
            print("| Lista de productos |".upper())
            print("======================")    
            for i in range(len(lista_productos)):
                print(f"{i + 1}. {lista_productos[i][0].capitalize()} - {lista_productos[i][1].capitalize()} - ${lista_productos[i][2]}")

        case "3":
            producto_buscado = input("Ingrese el nombre del producto que desea buscar: ").lower().strip()
            encontrado = False
            for producto in lista_productos:
                if producto[0] == producto_buscado:
                    print(f"Producto encontrado: {producto[0].capitalize()} - {producto[1].capitalize()} - ${producto[2]}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"Producto '{producto_buscado}' no encontrado en la lista.")

        case "4":
            for i in range(len(lista_productos)):
                print(f"{i + 1}. {lista_productos[i][0].capitalize()} - {lista_productos[i][1].capitalize()} - ${lista_productos[i][2]}")
                ## Verificar, solo muestra el primer producto de la lista!!.
            numero_producto = input("Ingrese el número del producto que desea eliminar: ")

            if numero_producto.isdigit():
                numero_producto = int(numero_producto)
                if numero_producto >= 1 and numero_producto <= len(lista_productos):
                    producto_eliminado = lista_productos.pop(numero_producto - 1)
                    print(f"Producto '{producto_eliminado[0].upper()}' eliminado exitosamente.")
                else:
                    print("Número de producto inválido.")
            else:
                print("Debe ingresar un número válido.")
           
        case "5": 
            print("Saliendo del sistema...")
            break
        case _: # Case default   
            print("Opción no válida. Por favor, seleccione una opción válida.")