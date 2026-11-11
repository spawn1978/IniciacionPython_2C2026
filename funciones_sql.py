from conexion import conectar

def registrar_producto(nombre, descripcion, categoria, cantidad, precio):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio)
                VALUES (?, ?, ?, ?, ?)
            ''', (nombre, descripcion, categoria, cantidad, precio))
            conn.commit()
            print("Producto registrado exitosamente.")
        except Exception as e:
            print(f"Error al registrar el producto: {e}")
        finally:
            cursor.close()
            conn.close()

def listar_producto():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM productos
            ''')
            productos = cursor.fetchall()
            for producto in productos:
                print(producto)
        except Exception as e:
            print(f"Error al listar los productos: {e}")
        finally:
            cursor.close()
            conn.close()