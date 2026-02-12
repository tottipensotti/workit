"""Tabla"""

from tkinter import Tk, Widget, W, EW, ttk
from typing import Tuple, Union


class Tabla:
    """Clase para generar la tabla de registros"""
    def __init__(
        self,
        root: Union[Tk, Widget],
        columns: Tuple[str, ...]
    ) -> None:
        self.tree: ttk.Treeview = ttk.Treeview(
            root,
            show="headings",
            height=10,
            columns=columns
        )

        for col in columns:
            self.tree.heading(col, text=col)

        self.tree.column("#", width=30, anchor=W)
        self.tree.column("Ejercicio", width=160, anchor=W)
        self.tree.column("Peso (kg)", width=100, anchor=W)
        self.tree.column("Repeticiones", width=100, anchor=W)
        self.tree.column("Series", width=100, anchor=W)
        self.tree.column("Fecha", width=120, anchor=W)

    def mostrar(self) -> None:
        """Muestra la tabla de registros en la UI"""
        self.tree.grid(
            row=5,
            column=0,
            columnspan=5,
            padx=20,
            pady=(10, 20),
            sticky=EW
        )
