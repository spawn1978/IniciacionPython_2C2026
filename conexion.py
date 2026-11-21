#from colorama import Fore, Back, Style, init
from colorama import Fore, init, Back, Style
import funciones_sql
import sqlite3

init(autoreset=True)

# Abre y devuelve la conexión con la base de datos.
def conectar():
    try:
        conexion = sqlite3.connect('inventario.db')
        print(Fore.GREEN + "Conexión exitosa a la base de datos.")
        return conexion
    
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al conectar a la base de datos: {e}")
        return None

# Crea las tablas necesarias para guardar productos y ventas.
def crear_tabla():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("PRAGMA foreign_keys = ON")
        
        # Tabla de productos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio INTEGER NOT NULL
            )
        ''')
        
        # Tabla de ventas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ventas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto_id  INTEGER NOT NULL,
                cantidad INTEGER NOT NULL CHECK (cantidad > 0),
                precio INTEGER NOT NULL,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE RESTRICT
           )
        ''')
        
        conexion.commit()
        print(Fore.GREEN + "Tabla 'productos' creada exitosamente.")
    
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al crear la tabla: {e}")
    finally:
        conexion.close()

