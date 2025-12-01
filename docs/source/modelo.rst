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

      class Conexion {
         +connect()
         +close()
      }

      class SqlExecutor {
         +execute()
         +fetch_all()
      }

      class Registro {
         +create()
         +read()
         +update()
         +delete()
      }

      Conexion <|-- SqlExecutor
      SqlExecutor --> Registro

Modelo de datos
----------------

.. mermaid::

   erDiagram

      ejercicio {
         int id PK
         string nombre
         string tipo
         int duracion_min
         date fecha
      }