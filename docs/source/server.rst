Servidor UDP
=============

El módulo **Server** implementa un servidor UDP para recibir y almacenar logs
de forma distribuida. Permite que múltiples instancias de la aplicación envíen
sus logs a un servidor centralizado.

Submódulos
----------

Módulo Server
~~~~~~~~~~~~~~

Servidor UDP que escucha logs y los almacena en archivos.

.. automodule:: workit.server.server
   :members:
   :undoc-members:
   :show-inheritance:

Módulo Client
~~~~~~~~~~~~~~

Cliente UDP para enviar logs al servidor.

.. automodule:: workit.server.client
   :members:
   :undoc-members:
   :show-inheritance:

---
Diagrama de Arquitectura — Logging Distribuido
------------------------------------------------

.. mermaid::

   sequenceDiagram
      participant App as Aplicación
      participant Client as Cliente UDP
      participant Server as Servidor UDP
      participant File as Archivo de Logs
      
      App->>Client: send(log)
      Client->>Server: UDP Packet
      Server->>File: Escribir log
      Server->>Client: ACK
      Client->>App: Confirmación
