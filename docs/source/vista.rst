Vista
=====

La capa **Vista** es responsable de toda la interacción visual con el usuario,
implementada usando **Tkinter**. Su función es:

- Renderizar formularios y tablas.
- Mostrar información proveniente del controlador.
- Capturar eventos del usuario.

No contiene reglas del negocio ni acceso directo a los datos.

Submódulos
----------

Módulo App
~~~~~~~~~~~

Punto de entrada visual de la aplicación. Inicializa y organiza la interfaz.

.. automodule:: workit.vista.app
   :members:
   :undoc-members:
   :show-inheritance:

Módulo Componentes
~~~~~~~~~~~~~~~~~~

Contiene widgets reutilizables: botones, etiquetas, entradas, etc.

.. automodule:: workit.vista.componentes
   :members:
   :undoc-members:
   :show-inheritance:

Módulo Formulario
~~~~~~~~~~~~~~~~~

Gestiona los formularios de carga y edición de ejercicios.

.. automodule:: workit.vista.formulario
   :members:
   :undoc-members:
   :show-inheritance:

Módulo Tabla
~~~~~~~~~~~~~

Muestra los registros existentes en formato tabular.

.. automodule:: workit.vista.tabla
   :members:
   :undoc-members:
   :show-inheritance:

---

Diagrama UML — Vista
--------------------

.. mermaid::

   classDiagram

      class App {
         +run()
      }

      class Header

      class Formulario {
         +get_data()
         +clear()
      }

      class Tabla {
         +update()
      }

      App --> Header
      App --> Formulario
      App --> Tabla