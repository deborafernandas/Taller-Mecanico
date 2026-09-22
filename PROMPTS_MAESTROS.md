# 📘 Guía Maestra de Prompts: Proyecto Taller Mecánico

Este documento contiene la secuencia exacta de **prompts mega detallados** que se utilizaron para construir la arquitectura del software de Taller Mecánico desde cero hasta su estado actual. 

Cualquier persona (o IA) que siga estos prompts en orden, logrará recrear exactamente la misma estructura de carpetas, código orientado a objetos, herencia, conexión a SQLite y el patrón Data Access Object (DAO) del proyecto.

---

## 🏗️ FASE 1: Construcción del Dominio (Clases y Herencia)

**Prompt 1: Creación de la clase base**
> "Actúa como un desarrollador Python experto. Crea un archivo llamado `vehiculo.py` con una clase `Vehiculo`. Debe tener un constructor que inicialice los atributos privados `__patente` (texto), `__anio` (entero) y `__en_taller` (booleano, por defecto falso). Agrega métodos `ingresar()` y `entregar()` que modifiquen el estado validando que no se pueda ingresar si ya está en el taller (y viceversa). Agrega un método `tarifa_hora()` que retorne un valor numérico de 5000. Comenta cada línea explicando su función."

**Prompt 2: Implementación de la Herencia (Subclases)**
> "Crea tres archivos nuevos para representar tipos de vehículos que hereden de la clase Vehiculo: `auto.py`, `moto.py` y `camion.py`. 
> - En `auto.py`, la clase `Auto` debe invocar al `super().__init__` y agregar el atributo privado `__capacidad_maletero`. Sobrescribe `tarifa_hora` para retornar 25000.
> - En `camion.py`, la clase `Camion` invoca a `super()` y agrega `__capacidad_carga`. Sobrescribe `tarifa_hora` para retornar 40000.
> - En `moto.py`, la clase `Moto` solo hereda la estructura base pero sobrescribe `tarifa_hora` para retornar 15000."

*(Nota: De manera similar se utilizaron prompts para crear el resto de las clases del modelo de negocio: `persona.py`, `cliente.py`, `usuario.py`, `rol.py`, `marca.py`, `modelo.py`, `ordentrabajo.py`, etc., definiendo sus constructores y relaciones de agregación/composición).*

---

## 📂 FASE 2: Refactorización de Arquitectura (MVC)

**Prompt 3: Ordenando el proyecto**
> "Crea 2 carpetas en la raíz del proyecto llamadas `model` y `dao`. Dentro de cada una, crea un archivo `__init__.py` vacío para convertirlas en paquetes de Python. A continuación, mueve todos los archivos de las clases del negocio (como `vehiculo.py`, `auto.py`, `marca.py`, etc.) a la carpeta `model`. Corrige todos los `import` en el proyecto para que incluyan la ruta del paquete (por ejemplo, `from model.vehiculo import Vehiculo`). No modifiques la lógica del código, solo la arquitectura."

---

## 🔌 FASE 3: Conexión a Base de Datos SQLite

**Prompt 4: Script de conexión**
> "Crea (o modifica) el archivo `conectar.py` en la raíz del proyecto. Debes importar la librería `sqlite3`. Dentro, define un método llamado `crear_conexion()` que no reciba parámetros. Este método debe realizar la conexión a una base de datos local llamada `taller.db`. Además, debe habilitar explícitamente el uso de Claves Foráneas (Foreign Keys) ejecutando el PRAGMA correspondiente, y finalmente debe retornar el objeto de la conexión."

---

## 🗄️ FASE 4: Implementación del Patrón DAO (Data Access Object)

**Prompt 5: DAO Base**
> "Vamos a crear nuestro primer DAO. Crea un archivo llamado `dao.py` dentro de la carpeta `dao`. Este archivo va a tener una clase `Dao` con un constructor `__init__` que reciba un objeto de conexión. Además de guardar esa conexión como un atributo de instancia, el constructor debe establecer y guardar un cursor a partir de dicha conexión para ser reutilizado. Documenta la clase."

**Prompt 6: DAO para Marcas (Tabla Independiente)**
> "Crea un archivo llamado `marca_dao.py` en la carpeta `dao`. Debe importar la clase base desde `dao.py`. Crea una clase `MarcaDao` que herede de `Dao`. Debe tener un método llamado `crear_tabla` que utilice el cursor heredado para ejecutar un CREATE TABLE IF NOT EXISTS para la tabla `marcas`. La tabla debe tener dos campos: `id` de tipo entero, primary key y autoincrementable; y `nombre` de tipo texto, not null."

**Prompt 7: DAO para Modelos (Con Clave Foránea)**
> "Ahora vamos por `ModeloDao` en el archivo `modelo_dao.py`. Misma estructura heredando de `Dao`. Su método `crear_tabla` debe crear la tabla `modelos` con los campos: `id` (entero, pk y autoincrementable), `nombre` (texto y not null), y `marca_id` (entero, not null). Además, `marca_id` debe configurarse como FOREIGN KEY referenciando al campo `id` de la tabla `marcas`."

**Prompt 8: DAO para Vehículos (Padre en la Herencia Relacional)**
> "Vamos ahora con `VehiculoDao` en el archivo `vehiculo_dao.py`. Crea una clase que herede de `Dao` y en su método `crear_tabla` construya la tabla `vehiculos` con los campos: `patente` (texto y primary key), `anio` (entero y not null), `en_taller` (entero) y `modelo_id` (entero y not null). Define `modelo_id` como foreign key de la tabla `modelos`."

**Prompt 9: DAO para Autos (Hijo en la Herencia Relacional / Table-per-type)**
> "Y ahora vamos con `AutoDao` en el archivo `auto_dao.py`. Este DAO es distinto: debe heredar de `VehiculoDao` (no de Dao directamente). Debe tener el método `crear_tabla`, pero lo primero que debe hacer es invocar a `super().crear_tabla()` para garantizar que la tabla padre exista. Luego, debe crear la tabla `autos` con un único campo: `patente` de tipo texto, el cual debe ser Primary Key y, al mismo tiempo, Foreign Key referenciando a `patente` de la tabla `vehiculos`."

---

## 🚀 FASE 5: Script Principal y Documentación

**Prompt 10: Ejecución de creación de tablas**
> "Modifica el archivo `main.py` en la raíz. Elimina cualquier lógica antigua y déjalo exclusivo para probar la base de datos. Debe: importar `conectar` y los DAOs `MarcaDao`, `ModeloDao` y `AutoDao`. Debe instanciar la conexión, instanciar los DAOs pasándoles la conexión, y llamar a sus métodos `crear_tabla()`. Finalmente, haz una consulta a `sqlite_master` para validar e imprimir en consola que las tablas `marcas`, `modelos`, `vehiculos` y `autos` se crearon exitosamente."

**Prompt 11: Documentación Didáctica**
> "Como paso final para el proceso educativo: por favor comenta cada una de las líneas de código lógico de todos los scripts que construimos hoy (`conectar.py`, los 5 archivos DAO, y `main.py`). Agrega un comentario en cada línea de Python explicando paso a paso qué hace esa línea. No modifiques la lógica."
