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
        
        
def nombre_actualizado(nuevo_nombre, id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE productos 
            SET nombre = ? 
            WHERE id = ? """,(nuevo_nombre,id))
        conn.commit()
    except Exception as e:
        print(Fore.RED + f"Error al actualizar los productos: {e}")
        return None
    finally:
        conn.close()
        
def descripcion_actualizado(nueva_descripcion,id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE productos 
            SET descripcion = ? 
            WHERE id = ? ''',(nueva_descripcion,id))
        conn.commit()
    except Exception as e:
        print(Fore.RED + f"Error al actualizar los productos: {e}")
        return None
    finally:
        conn.close()

def categoria_actualizado(nueva_categoria, id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE productos 
            SET categoria = ? 
            WHERE id = ? ''', (nueva_categoria, id))
        conn.commit()
    except Exception as e:
        print(Fore.RED + f"Error al actualizar los productos: {e}")
        return None
    finally:
        conn.close()

def cantidad_actualizado(nueva_cantidad, id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE productos 
            SET cantidad = ? 
            WHERE id = ? ''',(nueva_cantidad, id))
        conn.commit()
    except Exception as e:
        print(Fore.RED + f"Error al actualizar los productos: {e}")
        return None
    finally:
        conn.close()
        
def precio_actualizado(nuevo_precio, id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE productos 
            SET precio = ? 
           WHERE id = ? ''', (nuevo_precio, id))
        conn.commit()
    except Exception as e:
        print(Fore.RED + f"Error al actualizar los productos: {e}")
        return None
    finally:
        conn.close()
        
        
def producto_eliminado(producto_buscado):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM productos WHERE id = ?", (producto_buscado,))
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
