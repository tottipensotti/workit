Utilidades
===========

El módulo **Utils** contiene utilidades transversales que son utilizadas por diferentes
capas de la aplicación, implementando patrones de diseño comunes.

Submódulos
----------

Módulo Decoradores
~~~~~~~~~~~~~~~~~~~

Contiene decoradores reutilizables para validación y logging.

.. automodule:: workit.utils.decoradores
   :members:
   :undoc-members:
   :show-inheritance:

Módulo Observadores
~~~~~~~~~~~~~~~~~~~~

Implementa el patrón Observer para el sistema de logging distribuido.

.. automodule:: workit.utils.observadores
   :members:
   :undoc-members:
   :show-inheritance:

---
Diagrama UML — Patrón Observer
-------------------------------

.. mermaid::

   classDiagram
      class Sujeto {
         +suscribe(observador)
         +unsuscribe(observador)
         +notify(evento)
      }
      
      class Observador {
         <<abstract>>
         +update(evento)
      }
      
      class RegistroConsola
      class RegistroArchivo
      class RegistroServidor
      
      Sujeto o-- Observador : contiene
      Observador <|-- RegistroConsola
      Observador <|-- RegistroArchivo
      Observador <|-- RegistroServidor
