# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel  
**Institución:** Inacap  

---

## Bitácora de Avances

### 22 de Septiembre de 2026
- **Sincronización e Integración de Arquitectura Completa:**
  - Fusión de los avances del repositorio del docente (`michaelarjelm/Taller-Mecanico.git`), incorporando el paquete `dao` con la herencia relacional (`Dao`, `MarcaDao`, `ModeloDao`, `VehiculoDao`, `AutoDao`), el módulo de conexión con soporte de Foreign Keys (`conectar.py`), la reorganización de todas las clases de negocio en el paquete `model` y el documento de referencia `PROMPTS_MAESTROS.md`.
  - Se mantuvieron de forma armónica las validaciones de negocio en `model/vehiculo.py` (patente y rango de años 1900-2027) y en `model/auto.py` (capacidad de maletero y restricción vehicular).
- **Implementación de Consultas SELECT y Métodos CRUD en Capa DAO:**
  - **`model/modelo.py`:** Incorporación del atributo `__id` con su `@property` y setter para mapear la clave primaria autoincremental de la base de datos.
  - **`model/marca.py`:** Incorporación del setter para el atributo `nombre` permitiendo la modificación del estado del objeto de dominio.
  - **`dao/marca_dao.py`:**
    - Método `buscar(id)`: ejecuta `SELECT ... WHERE id = ?`, obtiene el registro con `fetchone()` y reconstruye el objeto `Marca`, retornando `None` si no existe.
    - Método `listar()`: ejecuta `SELECT id, nombre FROM marcas` con `fetchall()` y retorna la lista completa de instancias de `Marca`.
    - Método `actualizar(nueva_marca)`: ejecuta `UPDATE marcas SET nombre = ? WHERE id = ?`, valida con `cursor.rowcount > 0` la existencia y modificación del registro, realiza el `commit()` y retorna el registro fresco usando `buscar(nueva_marca.id)` (retornando `None` si el ID no existe).
  - **`dao/modelo_dao.py`:**
    - Método `insertar(modelo)`: guarda el nombre y la clave foránea `marca_id` obtenida de `modelo.marca.id`, actualizando el `modelo.id` generado.
    - Método `buscar(id)` con `INNER JOIN`: une `modelos` con `marcas` para recuperar en una sola consulta relacional la jerarquía completa y reconstruir tanto el objeto `Marca` como el objeto `Modelo`.
  - **`dao/vehiculo_dao.py`:**
    - Método `insertar(vehiculo)`: gestiona la persistencia en la tabla base `vehiculos` guardando `patente`, `anio`, `en_taller` y `modelo_id`.
  - **`dao/auto_dao.py`:**
    - Método `insertar(auto)`: aprovecha la herencia invocando a `super().insertar(auto)` para poblar la tabla padre `vehiculos` y registra la clave en la tabla hija `autos` (Table-per-type).
    - Método `buscar(patente)` con multi-JOIN: realiza `INNER JOIN` entre `autos`, `vehiculos`, `modelos` y `marcas`, reconstruyendo toda la jerarquía de objetos (`Marca` -> `Modelo` -> `Auto`) con sus métodos polimórficos (`tarifa_hora()`).
- **Actualización y Validación Integral (`main.py`):**
  - Se estructuró un flujo de pruebas que inicializa las tablas, inserta registros encadenados (`Marca` -> `Modelo` -> `Auto`), valida las búsquedas por ID y patente mediante JOINs y comprueba el retorno controlado de `None` ante identificadores inexistentes.

---

### 21 de Septiembre de 2026
- **Implementación de método de Inserción (CRUD):**
  - **`marca_dao.py`:** Se agregó el método `insertar()` para registrar nuevas marcas en la base de datos y recuperar el ID generado automáticamente mediante `lastrowid`.
  - **`marca.py`:** Se actualizó el modelo para incluir el atributo `id` con sus respectivos métodos *getter* y *setter*.
- **Actualización de Script Principal (`main.py`):**
  - Se adaptó el código para probar específicamente la inserción de una `Marca`, demostrando cómo el `id` pasa de `None` a un número válido tras guardar en la base de datos.
  - El código de creación de tablas original fue comentado para que sirva de referencia de estudio a los alumnos.

---

### 15 de Septiembre de 2026
- **Integración con SQLite y Habilitación de Foreign Keys:**
  - Creación del archivo `conectar.py` con la función `crear_conexion()` que establece la conexión a la base de datos `taller.db` y habilita el uso de Foreign Keys (`PRAGMA foreign_keys = ON`).
- **Refactorización de Arquitectura (MVC/DAO):**
  - Creación de los paquetes `model` y `dao`, añadiendo en ambos el archivo `__init__.py`.
  - Migración de todas las clases del dominio (vehículos, personas, órdenes, repuestos, etc.) a la carpeta `model` y actualización masiva de los imports en el proyecto.
- **Implementación del Patrón DAO (Data Access Object):**
  - **`dao.py` (Clase Base):** Gestiona la recepción de la conexión y establece el cursor para ser reutilizado.
  - **`marca_dao.py` y `modelo_dao.py`:** Clases hijas que heredan de `Dao` e incluyen el método `crear_tabla()`. Implementan llaves foráneas (FK) relacionando un Modelo a una Marca.
  - **`vehiculo_dao.py` y `auto_dao.py`:** Implementación de herencia relacional (Table-per-type). `AutoDao` hereda de `VehiculoDao` e invoca `super().crear_tabla()`. La tabla `autos` usa su llave primaria también como llave foránea hacia `vehiculos`.
- **Actualización de Script Principal (`main.py`):**
  - El código de prueba fue refactorizado y limpiado para enfocarse únicamente en inicializar los DAOs y crear (o validar la existencia de) las tablas correspondientes (`marcas`, `modelos`, `vehiculos`, `autos`).

---

### 14 de Septiembre de 2026
- **Integración Inicial con Base de Datos SQLite (`conectar.py`):**
  - Se creó el archivo `conectar.py` para gestionar la conexión y operaciones con una base de datos SQLite local (`taller.db`).
  - Se creó la tabla `Vehiculo` con los campos `patente` (TEXT, clave primaria), `modelo` (TEXT) y `en_taller` (INTEGER), usando `CREATE TABLE IF NOT EXISTS` para evitar errores si ya existe.
  - Se realizaron pruebas de inserción parametrizada y consulta `SELECT`.

---

### 8 de Septiembre de 2026
- **Clases y Métodos Abstractos (Abstracción con ABC):**
  - **Clase Vehiculo (`vehiculo.py`):** Se convirtió en clase abstracta heredando de `ABC` (`from abc import ABC, abstractmethod`).
  - Se definió `tarifa_hora()` como método abstracto mediante el decorador `@abstractmethod` con tipado de retorno `-> int`, estableciendo la obligación contractual de implementación para las subclases e impidiendo la instanciación directa de `Vehiculo`.
- **Encapsulamiento Seguro del Año (`@property` y `@anio.setter`):**
  - **Clase Vehiculo (`vehiculo.py`):** Se implementaron el getter y setter para `anio`, validando que el año de fabricación esté entre 1900 y 2027 (lanzando `ValueError` en caso contrario), y asignándolo desde el constructor `__init__` mediante `self.anio = anio`.
  - **Clase Auto (`auto.py`):** Se refactorizó la propiedad `restriccion` para interactuar limpiamente a través de `self.anio`, eliminando el uso de *name mangling* (`self._Vehiculo__anio`).
- **Manejo Resiliente de Excepciones y Pruebas (`main.py`):**
  - Se estructuraron bloques `try...except` controlados para demostrar la robustez del sistema ante:
    1. Intento de instanciar directamente la clase abstracta `Vehiculo` (`TypeError`).
    2. Validación de patente en el constructor al rechazar patentes cortas o con espacios (`ValueError`).
    3. Validación de año en el constructor al rechazar años fuera del rango 1900-2027 (`ValueError`).
    4. Simulación de ingreso de un auto antiguo (año 2008) registrando de forma controlada el aviso de restricción vehicular (`ValueError`).
- **Documentación:**
  - Se mantuvieron y actualizaron comentarios explicativos línea por línea con fines educativos.

---

### 7 de Septiembre de 2026
- **Sobrescritura de Métodos (Polimorfismo):**
  - **Clase Auto (`auto.py`):** Se sobrescribió el método `tarifa_hora()` para retornar un valor entero de `25000`.
  - **Clase Moto (`moto.py`):** Se implementó y sobrescribió el método `tarifa_hora()` retornando un valor entero de `15000`.
  - **Clase Camion (`camion.py`):** Se sobrescribió el método `tarifa_hora()` retornando un valor entero de `40000`.
  - Se mantuvo intacto el método `tarifa_hora()` en la clase base `Vehiculo` (`vehiculo.py`) retornando su valor base de `5000`.
- **Encapsulamiento y Validaciones con Properties (`@property`):**
  - **Clase Vehiculo (`vehiculo.py`):**
    - Se implementó la *property* `patente` (getter) para acceder al atributo privado `__patente`.
    - Se implementó el *setter* para `patente`, validando que posea al menos 6 caracteres y no contenga espacios, lanzando `ValueError` si no cumple.
    - Se actualizó el constructor `__init__` para asignar mediante `self.patente = patente`, aplicando la validación desde la instanciación de cualquier objeto.
  - **Clase Auto (`auto.py`):**
    - Se implementó la *property* `restriccion` (getter) para consultar el año del auto.
    - Se implementó el *setter* para `restriccion`, validando que el año sea mayor a 2011 (`> 2011`) con el mensaje `"auto sin restriccion vehicular"`, o lanzando un `ValueError` con el mensaje `"auto sujeto a restriccion vehicular"`.

---

### 31 de Agosto de 2026
- **Creación de Rama de Trabajo:** Creación y publicación de la rama `feature/desarrollo`.
- **Implementación de Herencia (Subclases):**
  - Se crearon tres clases derivadas a partir de la clase base `Vehiculo`:
    - **Clase Auto (`auto.py`):** Hereda de `Vehiculo`, implementa su propio constructor invocando a `super()` y añade el atributo privado `__capacidad_maletero` (en litros).
    - **Clase Moto (`moto.py`):** Hereda de `Vehiculo` (estructura base).
    - **Clase Camion (`camion.py`):** Hereda de `Vehiculo`, implementa su propio constructor invocando a `super()` y añade el atributo privado `__capacidad_carga` (en kilos).
- **Actualización de Script Principal (`main.py`):**
  - Se importaron las subclases `Auto`, `Moto` y `Camion`.
  - Se instanciaron objetos de cada una de las clases hijas y se verificó la invocación de métodos heredados (`ingresar()` y `tarifa_hora()`).
- **Documentación:** Código comentado línea por línea con fines pedagógicos.

---

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
