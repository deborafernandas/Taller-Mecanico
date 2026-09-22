# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel  
**Institución:** Inacap  

---

## Bitácora de Avances

### 25 de Agosto de 2026
- **Configuración Inicial:** Vinculación del directorio local con el repositorio de GitHub usando el CLI de GitHub (`gh auth`).
- **Limpieza:** Se eliminó la versión antigua del archivo `vehiculo.py` para construir el proyecto desde cero.
- **Clase Vehiculo (`vehiculo.py`):**
  - Se creó la clase principal del proyecto.
  - Se definieron los atributos privados `__patente`, `__anio` y `__en_taller` en el constructor, aplicando encapsulamiento y *type hints*.
  - Se crearon los métodos `ingresar()` y `entregar()` con validación de estado.
  - Se creó el método `tarifa_hora()` que retorna un valor fijo de 5000.
- **Script de Pruebas (`main.py`):**
  - Se creó el archivo de ejecución principal.
  - Se importó la clase `Vehiculo` y se instanciaron 3 objetos con datos ficticios.
  - Se probó la invocación de métodos y la impresión de la tarifa por hora en consola.
- **Documentación:** Se comentaron todas las líneas de código en ambos archivos (`vehiculo.py` y `main.py`) explicando paso a paso su funcionamiento con fines educativos.

---

### 31 de Agosto de 2026
- **Creación de Rama de Trabajo:** Creación y publicación de la rama `feature/desarrollo`.
- **Implementación de Herencia (Subclases):**
  - **Clase Auto (`auto.py`):** Hereda de `Vehiculo`, implementa su propio constructor invocando a `super()` y añade el atributo privado `__capacidad_maletero` (en litros).
  - **Clase Moto (`moto.py`):** Hereda de `Vehiculo` (estructura base).
  - **Clase Camion (`camion.py`):** Hereda de `Vehiculo`, implementa su propio constructor invocando a `super()` y añade el atributo privado `__capacidad_carga` (en kilos).
- **Actualización de Script Principal (`main.py`):**
  - Se importaron las subclases `Auto`, `Moto` y `Camion`.
  - Se instanciaron objetos de cada una de las clases hijas y se verificó la invocación de métodos heredados (`ingresar()` y `tarifa_hora()`).
- **Documentación:** Código comentado línea por línea con fines pedagógicos.

---

### 14 de Septiembre de 2026
- **Integración con Base de Datos SQLite (`conectar.py`):**
  - Se creó el archivo `conectar.py` para gestionar la conexión y operaciones con una base de datos SQLite local (`taller.db`).
  - Se estableció la conexión a la base de datos con `sqlite3.connect("taller.db")`.
  - Se creó la tabla `Vehiculo` con los campos `patente` (TEXT, clave primaria), `modelo` (TEXT) y `en_taller` (INTEGER), usando `CREATE TABLE IF NOT EXISTS` para evitar errores si ya existe.
  - Se instanciaron objetos de las clases `Marca`, `Modelo` y `Auto` para preparar datos de prueba (Toyota Yaris, patente AB1235).
  - Se realizó un `INSERT` de un vehículo en la tabla, pasando los valores como tupla de parámetros para prevenir inyección SQL.
  - Se realizó una consulta `SELECT` filtrando por patente para verificar la inserción correcta.
  - Se utilizó `fetchone()` para recuperar el registro y se imprimió en consola.
  - Se corrigió un bug: los valores del `INSERT` estaban pasados como argumentos separados en lugar de una tupla, generando `TypeError`.
- **Archivos involucrados:** `conectar.py`, `marca.py`, `modelo.py`, `auto.py`, `vehiculo.py`.

---

### 15 de Septiembre de 2026
- **Integración con SQLite:**
  - Creación del archivo `conectar.py` con una función `crear_conexion()` que establece la conexión a la base de datos `taller.db` y habilita el uso de Foreign Keys (`PRAGMA foreign_keys = ON`).
- **Refactorización de Arquitectura (MVC/DAO):**
  - Creación de los paquetes (carpetas) `model` y `dao`, añadiendo en ambos el archivo `__init__.py`.
  - Migración de todas las clases del dominio (vehículos, personas, órdenes, etc.) a la carpeta `model` y actualización masiva de los imports en el proyecto.
- **Implementación del Patrón DAO (Data Access Object):**
  - **`dao.py` (Clase Base):** Gestiona la recepción de la conexión y establece el cursor para ser reutilizado.
  - **`marca_dao.py` y `modelo_dao.py`:** Clases hijas que heredan de `Dao` e incluyen el método `crear_tabla()`. Implementan llaves foráneas (FK) relacionando un Modelo a una Marca.
  - **`vehiculo_dao.py` y `auto_dao.py`:** Implementación de herencia relacional (Table-per-type). `AutoDao` hereda de `VehiculoDao` e invoca `super().crear_tabla()`. La tabla `autos` usa su llave primaria también como llave foránea hacia `vehiculos`.
- **Actualización de Script Principal (`main.py`):**
  - El código de prueba fue refactorizado y limpiado para enfocarse únicamente en inicializar los DAOs y crear (o validar la existencia de) las tablas correspondientes (`marcas`, `modelos`, `vehiculos`, `autos`).
