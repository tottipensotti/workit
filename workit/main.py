"""Entrypoint de la aplicación"""

from vista import AppUI

app = AppUI('workit')

if __name__ == "__main__":
    app.inicializar_app()