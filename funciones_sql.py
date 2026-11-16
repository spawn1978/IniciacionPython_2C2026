from conexion import conectar
from colorama import Fore

# Guarda un producto nuevo en la tabla productos.
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

# Devuelve todos los productos ordenados por su ID.
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
        
# Busca y devuelve el producto que tiene el ID indicado.
def producto_buscado(id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, nombre, descripcion, categoria, cantidad, precio
            FROM productos WHERE id = ?
        ''', (id,))
        return cursor.fetchall()
    except Exception as e:
        print(Fore.RED + f"Error al listar los productos: {e}")
        return None
    finally:
        conn.close()
        
# Cambia el nombre del producto cuyo ID se recibe.
def nombre_actualizado(nuevo_nombre, id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        if cursor.fetchone() is None:
            raise ValueError(f"No existe el ID del producto: {id}")

        cursor.execute("""
            UPDATE productos 
            SET nombre = ? 
            WHERE id = ? """,(nuevo_nombre,id))
        conn.commit()
    except ValueError as e:
        print(Fore.RED + str(e))
        return None
    except Exception as e:
        print(Fore.RED + f"Error al actualizar los productos: {e}")
        return None
    finally:
        conn.close()
# Cambia la descripción del producto cuyo ID se recibe.
def descripcion_actualizado(nueva_descripcion,id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        if cursor.fetchone() is None:
            raise ValueError(f"No existe el ID del producto: {id}")
                
        cursor.execute('''
            UPDATE productos 
            SET descripcion = ? 
            WHERE id = ? ''',(nueva_descripcion,id))
        conn.commit()
    except ValueError as e:
        print(Fore.RED + str(e))
        return None
    except Exception as e:
        print(Fore.RED + f"Error al actualizar los productos: {e}")
        return None
    finally:
        conn.close()

# Cambia la categoría del producto cuyo ID se recibe.
def categoria_actualizado(nueva_categoria, id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        if cursor.fetchone() is None:
            raise ValueError(f"No existe el ID del producto: {id}")
                
        cursor.execute('''
            UPDATE productos 
            SET categoria = ? 
            WHERE id = ? ''', (nueva_categoria, id))
        conn.commit()
    except ValueError as e:
            print(Fore.RED + str(e))
            return None
    except Exception as e:
        print(Fore.RED + f"Error al actualizar los productos: {e}")
        return None
    finally:
        conn.close()

# Cambia la cantidad disponible del producto cuyo ID se recibe.
def cantidad_actualizado(nueva_cantidad, id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        if cursor.fetchone() is None:
            raise ValueError(f"No existe el ID del producto: {id}")

        cursor.execute('''
            UPDATE productos 
            SET cantidad = ? 
            WHERE id = ? ''',(nueva_cantidad, id))
        conn.commit()
    except ValueError as e:
        print(Fore.RED + str(e))
        return None
    except Exception as e:
        print(Fore.RED + f"Error al actualizar los productos: {e}")
        return None
    finally:
        conn.close()
# Cambia el precio del producto cuyo ID se recibe.
def precio_actualizado(nuevo_precio, id):
    conn = conectar()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        if cursor.fetchone() is None:
            raise ValueError(f"No existe el ID del producto: {id}")
        
        cursor.execute('''
            UPDATE productos 
            SET precio = ? 
           WHERE id = ? ''', (nuevo_precio, id))
        conn.commit()
    except ValueError as e:
        print(Fore.RED + str(e))
        return None
    except Exception as e:
        print(Fore.RED + f"Error al actualizar los productos: {e}")
        return None
    finally:
        conn.close()
        
# Elimina el producto indicado por ID y devuelve su nombre.
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

# Devuelve los productos cuya cantidad es igual o menor al mínimo indicado.
def generar_reporte(cantidad_minima):
    conn = conectar()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor()
        cantidad_minima = int(cantidad_minima)
        cursor.execute(
            "SELECT id, nombre, descripcion, categoria, cantidad, precio "
            "FROM productos WHERE cantidad <= ? ORDER BY id",
            (cantidad_minima,),
        )
        productos = cursor.fetchall()
        if not productos:
            print(Fore.RED + f"No existen productos con una cantidad igual o inferior a la indicada: {cantidad_minima}")
            return []
        return productos
    except ValueError as e:
        print(Fore.RED + "La cantidad mínima debe ser un número entero.")
        return None
    except Exception as e:
        print(Fore.RED + f"Error al generar el reporte: {e}")
        return None
    finally:
        conn.close()
        

