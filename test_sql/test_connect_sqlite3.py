import sqlite3

# Establecer la conexión a la base de datos
conexion = sqlite3.connect("productos.db")
print("Conexión establecida exitosamente.")

# Cerrar la conexión
conexion.close()