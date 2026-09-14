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
