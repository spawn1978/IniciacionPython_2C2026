#!/usr/bin/env python3
# Sistema de Gestión de Productos

"""
Nombre del Módulo: main.py
Descripción: Este script agrega, visualiza, busca y elimina productos de una lista.
Autor: Carlos Leguizmaon
Fecha de Creación: 2026-10-04
Versión: 1.0.0
"""

#from funciones import agregar_productos, mostrar_productos
import funciones, funciones_sql, conexion

conexion.crear_tabla()

"""

lista_productos = [
    ["manazana", "fruta", "Fruta fresca", 3, 1000],
    ["pera", "fruta", "fruta fresca", 2, 2000],
    ["banana", "fruta", "fruta fresca", 5, 1500],
    ["pan molde", "panaderia", "pan fresco", 10, 500],
    ["leche", "lacteos", "leche fresca", 2, 3000],
    ["manteca", "lacteos", "manteca fresca", 1, 4000],
    ["queso", "lacteos", "queso fresco", 3, 6000]
]    
"""

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
            funciones.agregar_productos()
            
        case "2":
            # Mostrar productos
            funciones_sql.listar_producto()
            
        case "3":
            # Busqueda de producto
            producto_encontrados = funciones.buscar_productos(lista_productos)
            funciones.mostrar_productos(producto_encontrados)
            
        case "4":
            # Eliminar producto
            funciones.eliminar_producto(lista_productos)
            
        case "5": 
            print("Saliendo del sistema...")
            break
        case _: # Case default
                    try:
                        int(opcion)
                    except ValueError:
                        print("Debe ingresar una opción numérica.")
                    else:
                        print("Opción no válida. Por favor, seleccione una opción del menú.")