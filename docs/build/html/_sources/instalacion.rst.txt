Instalación y Uso
==================

Instalación
-----------

Workit requiere Python 3.11 o superior.

Instalación con uv (recomendado)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Clonar el repositorio
   git clone https://github.com/tottipensotti/workit.git
   cd workit

   # Instalar dependencias
   uv sync

   # Instalar dependencias de desarrollo (opcional)
   uv sync --dev

   # Instalar dependencias de documentación (opcional)
   uv sync --extra docs

Instalación con pip
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Instalar el paquete
   pip install -e .

Uso
---

Ejecutar la aplicación
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Con uv
   uv run workit

   # O directamente
   python -m workit.main

Generar documentación
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd docs
   make html

   # La documentación se generará en docs/build/html/

Ejecutar el servidor de logs (opcional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En una terminal:

.. code-block:: bash

   python -m workit.server.server

La aplicación enviará automáticamente los logs al servidor si está corriendo.

Dependencias
------------

- **peewee**: ORM para SQLite
- **tkcalendar**: Widget de calendario para Tkinter
- **babel**: Internacionalización

Dependencias opcionales
~~~~~~~~~~~~~~~~~~~~~~~

- **sphinx**: Generación de documentación
- **sphinx-rtd-theme**: Tema para documentación
- **sphinxcontrib-mermaid**: Diagramas Mermaid en documentación
