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
        except Exception as e:
            print(f"Error al registrar el producto: {e}")
        finally:
            cursor.close()
            conn.close()

def listar_producto():
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, nombre, descripcion, categoria, cantidad, precio
            FROM productos
            ORDER BY id
        ''')
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al listar los productos: {e}")
        return None
    finally:
        conn.close()
        
def producto_buscado(producto_buscado):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, nombre, descripcion, categoria, cantidad, precio
            FROM productos WHERE nombre LIKE ? ''', (f"%{producto_buscado}%",))
        return cursor.fetchall()
    except Exception as e:
        print(Fore.RED + f"Error al listar los productos: {e}")
        return None
    finally:
        conn.close()
def producto_eliminado(producto_buscado):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM productos WHERE nombre = ?", (producto_buscado,))
        producto = cursor.fetchone()
        if producto is None:
            return None

        cursor.execute("DELETE FROM productos WHERE id = ?", (producto[0],))
        conn.commit()
        return producto[1]
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")
        return None
    finally:
        conn.close()