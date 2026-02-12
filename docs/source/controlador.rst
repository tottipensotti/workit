Controlador
============

El **Controlador** orquesta la comunicación entre la Vista y el Modelo.

Sus responsabilidades incluyen:

- Gestionar eventos de botones y formularios.
- Validar datos entrantes usando decoradores.
- Llamar a las funciones del Modelo.
- Notificar eventos a los observadores (logging).
- Implementar el patrón Observer para logging distribuido.

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

      class Sujeto {
         +suscribe(observador)
         +notify(evento)
      }

      class Controlador {
         +agregar_registro(data)
         +modificar_registro(data)
         +borrar_registro(id)
         +consultar_registro()
      }

      class Executor
      class Observador

      Sujeto <|-- Controlador
      Controlador --> Executor
      Controlador --> Observador : notifica eventos