"""Clase Componentes"""

from tkinter import Button, Label, EW, Tk, Widget
from typing import Callable, Dict, Any, Union


class Boton:
    """Clase auxiliar para crear botones"""
    def __init__(
        self,
        root: Union[Tk, Widget],
        texto: str,
        color: str,
        comando: Callable[[], None]
    ) -> None:
        self.config_base: Dict[str, Any] = {
            "width": 20,
            "height": 2,
            "relief": "flat",
            "font": ("Segoe UI", 9, "bold"),
            "cursor": "hand2",
            "fg": "black",
            "highlightthickness": 0,
            "bd": 0
        }
        self.boton: Button = Button(
            root,
            text=texto,
            bg=color,
            command=comando,
            **self.config_base
        )

    def mostrar(self, row: int, column: int, **kwargs: Any) -> None:
        """Muestra el botón en la grilla"""
        self.boton.grid(row=row, column=column, **kwargs)


class Botonera:
    """Clase para generar la botonera"""
    def __init__(
        self,
        root: Union[Tk, Widget],
        agregar: Callable[[], None],
        modificar: Callable[[], None],
        borrar: Callable[[], None]
    ) -> None:
        self.boton_agregar: Boton = Boton(root, "Agregar", "light green", agregar)
        self.boton_modificar: Boton = Boton(root, "Modificar", "khaki1", modificar)
        self.boton_borrar: Boton = Boton(root, "Borrar", "light coral", borrar)

    def generar_botones(self) -> None:
        """Muestra los botones en la UI"""
        self.boton_agregar.mostrar(row=3, column=0, pady=8)
        self.boton_modificar.mostrar(row=3, column=1, pady=8)
        self.boton_borrar.mostrar(row=3, column=2, pady=8)


class Header:
    """Clase encabezado de la UI"""
    def __init__(self, root: Union[Tk, Widget], texto: str) -> None:
        self.encabezado: Label = Label(
            root,
            text=texto,
            bg="DarkOrchid3",
            fg="thistle1",
            font=("Segoe UI", 12, "bold"),
            height=2,
            width=80,
            anchor="center"
        )

    def mostrar(self) -> None:
        """Genera el encabezado en la UI"""
        self.encabezado.grid(
            row=0,
            column=0,
            columnspan=5,
            padx=1,
            pady=5,
            sticky=EW
        )
