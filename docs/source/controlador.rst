Controlador
============

El **Controlador** orquesta la comunicación entre la Vista y el Modelo.

Sus responsabilidades incluyen:

- Gestionar eventos de botones y formularios.
- Validar datos entrantes.
- Llamar a las funciones del Modelo.
- Actualizar la Vista con los resultados.

Submódulos
----------

Módulo Controlador
~~~~~~~~~~~~~~~~~~~

Encapsula la lógica principal de control de la aplicación.

.. automodule:: workit.controlador.controlador
   :members:
   :undoc-members:
   :show-inheritance:

---

Diagrama UML — Controlador
--------------------------

.. mermaid::

   classDiagram

      class Controlador {
         +crear()
         +modificar()
         +borrar()
         +listar()
      }

      Controlador --> Registro
      Controlador --> Formulario
      Controlador --> Tabla