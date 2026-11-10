import sqlite3

def conectar():
    try:
        conn = sqlite3.connect('inventario.db')
        print("Conexión exitosa a la base de datos.")
        return conn
    
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
def crear_tabla(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        ''')
        conn.commit()
        print("Tabla 'productos' creada exitosamente.")
    
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")