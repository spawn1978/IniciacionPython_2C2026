# Sistema de Gestión de Productos

Aplicación de consola en Python para registrar y administrar productos usando SQLite. Los datos se guardan en el archivo `inventario.db`, por lo que permanecen disponibles al cerrar y volver a iniciar el programa.

## Requisitos

- Python 3.
- SQLite, incluido en la biblioteca estándar de Python; no requiere instalar paquetes adicionales.

## Ejecutar

Desde la carpeta del proyecto, ejecutá:

```bash
python3 main.py
```

Al iniciar, el programa crea la tabla `productos` si todavía no existe.

## Menú

```text
Sistema de Gestión de Productos

1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir
```

### Agregar producto

Solicita nombre, descripción, categoría, cantidad y precio. El nombre, la descripción y la categoría no pueden quedar vacíos. La categoría debe contener letras; cantidad y precio deben ser números enteros positivos. Los nombres, descripciones y categorías se guardan en minúsculas.

### Mostrar productos

Muestra los productos registrados con su identificador, nombre, descripción, categoría, cantidad y precio. Si no hay productos, informa que la base está vacía.

### Buscar producto

Busca por nombre usando coincidencias parciales. Por ejemplo, buscar `pep` puede mostrar el producto `pepino`. Si no hay coincidencias, informa que no se encontraron productos.

### Eliminar producto

Solicita el nombre exacto del producto y muestra el nombre eliminado. La eliminación usa el identificador de la fila encontrada; si el nombre no existe, informa que no se encontró. Si hay productos con el mismo nombre, elimina uno por vez.

## Base de datos

La tabla `productos` contiene estas columnas:

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `id` | Entero | Identificador único autoincremental |
| `nombre` | Texto | Nombre del producto |
| `descripcion` | Texto | Descripción del producto |
| `categoria` | Texto | Categoría del producto |
| `cantidad` | Entero | Unidades disponibles |
| `precio` | Entero | Precio sin centavos |

## Organización del código

- `main.py`: muestra el menú y llama a la función correspondiente.
- `funciones.py`: solicita datos, valida entradas y presenta los resultados.
- `funciones_sql.py`: registra, lista, busca y elimina productos mediante consultas SQL.
- `conexion.py`: se conecta a `inventario.db` y crea la tabla `productos`.
