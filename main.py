#!/usr/bin/env python3
"""
Sistema de Gestión de Productos
Nombre del Módulo: main.py
Descripción: Este script agrega, visualiza, busca y elimina productos de una lista.
Autor: Carlos Leguizmaon
Fecha de Creación: 2026-10-04
Versión: 1.0.0
"""
import funciones, funciones_sql, conexion

conexion.crear_tabla()

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
        case "1": # Agregar producto OK
            funciones.agregar_productos()
            
        case "2":
            # Mostrar productos. OK
            funciones.mostrar_productos()
            
        case "3":
            # Busqueda de producto. OK
            funciones.buscar_producto()
            
        case "4":
            # Eliminar producto. OK
            funciones.eliminar_producto()
            
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