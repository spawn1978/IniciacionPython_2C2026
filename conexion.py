#from colorama import Fore, Back, Style, init
from colorama import Fore, init, Back, Style
import sqlite3

init(autoreset=True)

# Funcion conectar. Realiza la conexion a la base de datos
def conectar():
    try:
        conexion = sqlite3.connect('inventario.db')
        print(Fore.GREEN + "Conexión exitosa a la base de datos.")
        return conexion
    
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al conectar a la base de datos: {e}")
        return None

# Funcion crear_tabla. Crea tabla iniciarl    
def crear_tabla():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
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
        conexion.commit()
        print(Fore.GREEN + "Tabla 'productos' creada exitosamente.")
    
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al crear la tabla: {e}")
    finally:
        conexion.close()
