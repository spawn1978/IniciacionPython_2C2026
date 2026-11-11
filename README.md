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

## Funcionamiento de las funciones

### `main.py`

El archivo no define funciones. Al ejecutarse, llama a `crear_tabla()` para asegurar que la tabla exista y luego mantiene el menú dentro de un ciclo `while`. Según la opción elegida, llama a la función correspondiente de `funciones.py`; la opción 5 termina el ciclo.

### `funciones.py`

- `agregar_productos()`: pide nombre, descripción, categoría, cantidad y precio. Repite la solicitud si faltan nombre o descripción, si la categoría no contiene solo letras, o si cantidad/precio no son enteros positivos. Convierte a minúsculas los campos de texto y envía los datos a `funciones_sql.registrar_producto()`. No devuelve un valor.
- `mostrar_productos()`: solicita todas las filas a `funciones_sql.listar_producto()`. Informa si no hay productos; de lo contrario, imprime cada fila con sus seis campos. No devuelve un valor.
- `buscar_producto()`: pide un texto de búsqueda, lo limpia y convierte a minúsculas, y lo envía a `funciones_sql.producto_buscado()`. Imprime las coincidencias o un aviso si no hay resultados. No devuelve un valor.
- `eliminar_producto()`: pide el nombre del producto, lo limpia y convierte a minúsculas, y lo envía a `funciones_sql.producto_eliminado()`. Muestra el nombre eliminado o informa que no se encontró. No devuelve un valor.

### `funciones_sql.py`

Estas funciones realizan las consultas y cierran la conexión al terminar. Las consultas usan parámetros (`?`) para pasar los valores a SQLite.

- `registrar_producto(nombre, descripcion, categoria, cantidad, precio)`: inserta un registro en `productos` y confirma el cambio con `commit()`. Informa si se registró o si ocurrió un error. No devuelve un valor.
- `listar_producto()`: obtiene todos los productos ordenados por `id`. Devuelve una lista de tuplas, una por fila, con los campos `id`, `nombre`, `descripcion`, `categoria`, `cantidad` y `precio`. Devuelve `None` si no puede conectarse o si ocurre un error.
- `producto_buscado(producto_buscado)`: busca nombres que contengan el texto recibido (`LIKE`). Devuelve una lista de tuplas con los seis campos del producto, o una lista vacía si no hay coincidencias. Devuelve `None` ante un error de conexión o consulta.
- `producto_eliminado(producto_buscado)`: busca una fila cuyo nombre coincida exactamente con el texto recibido. `fetchone()` obtiene esa fila; si existe, elimina el producto usando su `id`, confirma el cambio y devuelve el nombre eliminado. Si no encuentra una fila o ocurre un error, devuelve `None`. Si hay nombres repetidos, elimina una sola fila.

### `conexion.py`

- `conectar()`: abre una conexión al archivo `inventario.db`. Devuelve el objeto de conexión si tiene éxito; en caso de error, muestra el mensaje y devuelve `None`.
- `crear_tabla()`: se conecta a la base y crea la tabla `productos` si todavía no existe, con las columnas detalladas arriba. Confirma la operación y muestra un mensaje. Se ejecuta al iniciar `main.py`.
