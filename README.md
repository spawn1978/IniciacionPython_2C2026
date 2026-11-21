# Sistema de Gestión de Productos

Aplicación de consola escrita en Python para registrar, consultar, actualizar y eliminar productos. Utiliza SQLite para guardar la información en el archivo `inventario.db`, ubicado en el directorio desde donde se ejecuta el programa.

## Requisitos

- Python 3.10 o posterior.
- `colorama` para mostrar mensajes con colores.
- SQLite, incluido en la biblioteca estándar de Python.

Instalar `colorama` si todavía no está disponible en el entorno:

```bash
python3 -m pip install colorama
```

## Ejecutar

Desde la carpeta del proyecto, ejecutá:

```bash
python3 main.py
```

## Menú principal

1. Agregar producto
2. Mostrar productos
3. Buscar producto por ID
4. Eliminar producto por ID
5. Actualizar producto
6. Generar reporte de stock
7. Salir

La opción 5 abre un submenú para actualizar el nombre, la descripción, la categoría, la cantidad o el precio. La opción 6 solicita una cantidad mínima y muestra los productos cuya cantidad disponible es igual o inferior a ese valor.

## Operaciones

### Agregar producto

Solicita nombre, descripción, categoría, cantidad y precio. El nombre y la descripción no pueden quedar vacíos; la categoría debe contener solamente letras. La cantidad y el precio deben ser números enteros positivos. Los campos de texto se guardan en minúsculas.

### Mostrar productos

Muestra todos los productos ordenados por ID, con nombre, descripción, categoría, cantidad y precio. Informa cuando no hay productos registrados.

### Buscar producto

Solicita un ID y muestra el producto correspondiente. Si el ID no existe, informa que no se encontraron resultados.

### Eliminar producto

Solicita el ID del producto. Si existe, elimina el registro y confirma la operación; si no existe, informa que no se encontró.

### Actualizar producto

Permite modificar un campo del producto seleccionado por ID. Antes de actualizar, las funciones SQL verifican que el producto exista. Si no existe, informan que el ID del producto no existe.

### Generar reporte

Solicita un número entero y lista los productos con una cantidad disponible menor o igual a ese número. Si no hay productos que cumplan la condición, muestra un mensaje indicando que el reporte no tiene resultados.

## Base de datos

La tabla `productos` almacena los datos de cada producto:

| Columna | Tipo SQLite | Descripción |
| --- | --- | --- |
| `id` | `INTEGER` | Identificador único autoincremental |
| `nombre` | `TEXT` | Nombre del producto; no puede ser nulo |
| `descripcion` | `TEXT` | Descripción del producto |
| `categoria` | `TEXT` | Categoría; no puede ser nula |
| `cantidad` | `INTEGER` | Unidades disponibles; no puede ser nula |
| `precio` | `INTEGER` | Precio; no puede ser nulo |

La tabla `ventas` también se crea al iniciar:

| Columna | Tipo SQLite | Descripción |
| --- | --- | --- |
| `id` | `INTEGER` | Identificador único autoincremental |
| `producto_id` | `INTEGER` | ID del producto relacionado |
| `cantidad` | `INTEGER` | Unidades vendidas; debe ser mayor que cero |
| `precio` | `INTEGER` | Precio registrado para la venta |
| `fecha` | `TIMESTAMP` | Fecha y hora de creación; por defecto, la fecha actual |


## Archivos y funciones

### `main.py`

Crea las tablas al iniciar y muestra el menú principal. Gestiona las opciones, el submenú de actualización y la impresión de los resultados del reporte.

### `funciones.py`

- `agregar_productos()`: solicita y valida los datos de un producto y los envía para guardarlos.
- `mostrar_productos()`: obtiene y muestra la lista de productos.
- `buscar_producto()`: solicita un ID y muestra el producto encontrado.
- `eliminar_producto()`: solicita un ID y elimina el producto correspondiente.

### `funciones_sql.py`

Estas funciones realizan consultas parametrizadas a SQLite y cierran la conexión al terminar:

- `registrar_producto(nombre, descripcion, categoria, cantidad, precio)`: inserta un producto y confirma el cambio.
- `listar_producto()`: devuelve todos los productos ordenados por ID.
- `producto_buscado(id)`: devuelve el producto que coincide con el ID.
- `nombre_actualizado(nuevo_nombre, id)`: actualiza el nombre si el ID existe.
- `descripcion_actualizado(nueva_descripcion, id)`: actualiza la descripción si el ID existe.
- `categoria_actualizado(nueva_categoria, id)`: actualiza la categoría si el ID existe.
- `cantidad_actualizado(nueva_cantidad, id)`: actualiza la cantidad si el ID existe.
- `precio_actualizado(nuevo_precio, id)`: actualiza el precio si el ID existe.
- `producto_eliminado(producto_buscado)`: elimina el producto indicado por ID y devuelve su nombre.
- `generar_reporte(cantidad_minima)`: devuelve los productos cuya cantidad es menor o igual al valor indicado.

Las funciones de consulta devuelven `None` si no pueden conectarse o si ocurre un error. El reporte devuelve una lista vacía cuando la consulta se ejecuta correctamente pero no encuentra productos.

### `conexion.py`

- `conectar()`: abre y devuelve una conexión con `inventario.db`.
- `crear_tabla()`: crea las tablas `productos` y `ventas` si no existen y activa las claves foráneas en la conexión usada para crearlas.
