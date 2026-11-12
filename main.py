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
from colorama import Fore, Back, Style, init

init(autoreset=True)

conexion.crear_tabla()

# Menu de opciones de la aplicacion
while True:
    print("===================================")
    print("| Sistema de Gestión de Productos |".upper())
    print("===================================")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Actualizar producto")
    print("6. Salir")

    opcion = input("Seleccione una opción: ".strip())  

    match opcion:
        case "1": # Agregar producto
            funciones.agregar_productos()
            
        case "2":
            # Mostrar productos.
            funciones.mostrar_productos()
            
        case "3":
            # Busqueda de producto. 
            funciones.buscar_producto()
            
        case "4":
            # Eliminar producto. 
            funciones.eliminar_producto()
            
        case "5":
            # ACtualizar datos de producto
            while True:
                print("=======================================")
                print("| Actualizacion de Datos de Productos |".upper())
                print("=======================================")
                print("1. Actualizar Nombre")
                print("2. Actualizar Descripcion")
                print("3. Actualizar Categoria")
                print("4. Actualizar Cantidad")
                print("5. Actualizar Precio")
                print("6. Salir")
                
                opcion = input("Que dato desea actualizar: ".strip())  
            
                match opcion:
                    case "1": # Agregar producto
                            print("Actualizar Nombre")
                            #funciones.agregar_productos()
                                    
                    case "2":
                            print("Actualizar Descripcion")
                            #funciones.mostrar_productos()
                                    
                    case "3":
                            print("Actualizar Categoria")
                            #funciones.buscar_producto()
                                    
                    case "4":
                            print("Actualizar Cantidad")
                            #funciones.eliminar_producto()
                    case "5":
                            print("Actualizar Precio")
                            #funciones.eliminar_producto()
                                    
                    case "6":
                            print(Fore.GREEN + "Saliendo del submenu de actualizacion...")
                            break
                    case _: # Case default
                                try:
                                    int(opcion)
                                except ValueError:
                                    print(Fore.RED + "Debe ingresar una opción numérica.")
                                else:
                                    print(Fore.RED + "Opción no válida. Por favor, seleccione una opción del menú.")
                        
        case "6": 
            print("Saliendo del sistema...")
            break
        case _: # Case default
                    try:
                        int(opcion)
                    except ValueError:
                        print(Fore.RED + "Debe ingresar una opción numérica.")
                    else:
                        print(Fore.RED + "Opción no válida. Por favor, seleccione una opción del menú.")
