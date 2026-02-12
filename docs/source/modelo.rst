Modelo
=======

La capa **Modelo** centraliza toda la lógica de negocio de Workit y la interacción
con la base de datos. Es responsable de:

- Crear y administrar conexiones persistentes.
- Ejecutar operaciones SQL.
- Representar registros.
- Validar datos obtenidos desde la Vista.

Submódulos
----------

Módulo Conexion
~~~~~~~~~~~~~~~~

Gestiona la conexión a la base de datos SQLite y administra cursores.

.. automodule:: workit.modelo.conexion
   :members:
   :undoc-members:
   :show-inheritance:

Módulo Executor
~~~~~~~~~~~~~~~~

Ejecuta comandos SQL y encapsula la lógica de escritura y consulta sobre la base.

.. automodule:: workit.modelo.executor
   :members:
   :undoc-members:
   :show-inheritance:

Módulo Registro
~~~~~~~~~~~~~~~~

Representa las entidades principales del dominio del sistema.

.. automodule:: workit.modelo.registro
   :members:
   :undoc-members:
   :show-inheritance:

---

Diagrama UML — Modelo
---------------------

.. mermaid::

   classDiagram

      class SqliteDatabase {
         +connect()
      }

      class Executor {
         +consultar_bbdd()
         +agregar_bbdd(data)
         +borrar_bbdd(id)
         +modificar_bbdd(data)
      }

      class Registro {
         +id
         +ejercicio
         +peso
         +reps
         +series
         +fecha
      }

      SqliteDatabase --> Executor
      Executor --> Registro

Modelo de datos
----------------

.. mermaid::

   erDiagram

      Registro {
         int id PK
         string ejercicio
         float peso
         float reps
         int series
         string fecha
      }