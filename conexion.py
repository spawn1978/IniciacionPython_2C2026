import sqlite3

def conectar():
    try:
        conexion = sqlite3.connect('inventario.db')
        print("Conexión exitosa a la base de datos.")
        return conexion
    
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    
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
        print("Tabla 'productos' creada exitosamente.")
    
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.close()