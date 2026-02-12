"""Entrypoint de la aplicación"""

from workit.vista import App


def main() -> None:
    """Inicializa la aplicación"""
    app: App = App('Workit 💪')


if __name__ == "__main__":
    main()
