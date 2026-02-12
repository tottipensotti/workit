"""Clase Formulario"""

from tkinter import Label, StringVar, DoubleVar, Entry, Tk, Widget
from typing import List, Union
from tkcalendar import DateEntry


class Formulario:
    """Clase para crear etiquetas y entradas"""
    def __init__(
        self,
        root: Union[Tk, Widget],
        color: str,
        ancho_col: int
    ) -> None:
        self.root: Union[Tk, Widget] = root
        self.color: str = color
        self.ancho_col: int = ancho_col

        self.etiquetas: List[str] = [
            "Ejercicio", "Peso (kg)", "Repeticiones", "Series", "Fecha"
        ]
        self.values: List[tuple] = [
            (StringVar(), Entry),
            (DoubleVar(), Entry),
            (DoubleVar(), Entry),
            (DoubleVar(), Entry),
            (StringVar(), DateEntry)
        ]
        self.valor_ejercicio: StringVar = self.values[0][0]
        self.valor_peso: DoubleVar = self.values[1][0]
        self.valor_reps: DoubleVar = self.values[2][0]
        self.valor_series: DoubleVar = self.values[3][0]
        self.valor_fecha: StringVar = self.values[4][0]

        self.entradas: List[Union[Entry, DateEntry]] = self._get_entries()

    def _get_entries(self) -> List[Union[Entry, DateEntry]]:
        """Genero dinámicamente las entradas"""
        entradas: List[Union[Entry, DateEntry]] = []
        for valor, tipo in self.values:
            if tipo == Entry:
                entrada = tipo(
                    self.root,
                    textvariable=valor,
                    width=self.ancho_col,
                    relief="solid"
                )
            else:
                entrada = tipo(
                    self.root,
                    textvariable=valor,
                    width=self.ancho_col-2,
                    date_pattern="dd-mm-yyyy"
                )
            entradas.append(entrada)

        return entradas

    def crear(self) -> None:
        """Crea el formulario en la UI"""
        for i, etiqueta in enumerate(self.etiquetas):
            Label(
                self.root,
                text=etiqueta,
                bg=self.color,
                fg="black",
                font=("Segoe UI", 10, "bold")
            ).grid(row=1, column=i, padx=5, pady=(10, 2))

        for i, entrada in enumerate(self.entradas):
            entrada.grid(row=2, column=i, padx=20, pady=4, ipadx=3, ipady=3)

    def limpiar_formulario(self) -> None:
        """Limpia todos los campos del formulario"""
        self.valor_ejercicio.set("")
        self.valor_peso.set(0.0)
        self.valor_reps.set(0.0)
        self.valor_series.set(0.0)
        self.valor_fecha.set("")
