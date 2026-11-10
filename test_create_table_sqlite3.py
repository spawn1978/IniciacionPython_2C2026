import sqlite3

# Establecer la conexión a la base de datos
conexion = sqlite3.connect("productos.db")

# Crear un objeto cursor
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL)
''')
print("Tabla 'productos' creada exitosamente.")

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()