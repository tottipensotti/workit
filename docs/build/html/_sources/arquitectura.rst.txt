Arquitectura
=============

Workit está construida siguiendo el patrón **Modelo–Vista–Controlador (MVC)**.
Este enfoque divide la aplicación en tres responsabilidades bien definidas:

Modelo
-------

Contiene toda la lógica del negocio y el acceso a datos:

- Persistencia (conexión a base de datos).
- Operaciones CRUD.
- Normalización y validaciones.
- Exposición de datos al controlador.

Vista
------

Gestiona la interfaz gráfica:

- Formularios.
- Tablas.
- Botones.
- Renderizado de datos.

No contiene reglas del negocio ni acceso directo a la base de datos.

Controlador
------------

Actúa como intermediario entre el **Modelo** y la **Vista**:

- Recibe eventos del usuario.
- Solicita acciones al Modelo.
- Procesa resultados.
- Actualiza la Vista.

---

Diagrama MVC
------------

.. mermaid::

    flowchart LR
        Usuario --> Vista
        Vista --> Controlador
        Controlador --> Modelo
        Modelo --> Controlador
        Controlador --> Vista