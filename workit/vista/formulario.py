"""Clase Formulario"""
from tkinter import Label, StringVar, DoubleVar, Entry
from tkcalendar import DateEntry


class Formulario:
    """Clase para crear etiquetas y entradas"""
    def __init__(self, root, color, ancho_col):
        self.root = root
        self.color = color
        self.ancho_col = ancho_col

        self.valor_ejercicio = StringVar()
        self.valor_peso = DoubleVar()
        self.valor_reps = DoubleVar()
        self.valor_series = DoubleVar()
        self.valor_fecha = StringVar()
        self.etiquetas = ["Ejercicio", "Peso (kg)", "Repeticiones", "Series", "Fecha"]
        self.entradas = [
            Entry(self.root, textvariable=self.valor_ejercicio, width=self.ancho_col, relief="solid"),
            Entry(self.root, textvariable=self.valor_peso, width=self.ancho_col, relief="solid"),
            Entry(self.root, textvariable=self.valor_reps, width=self.ancho_col, relief="solid"),
            Entry(self.root, textvariable=self.valor_series, width=self.ancho_col, relief="solid"),
            DateEntry(self.root, textvariable=self.valor_fecha, width=self.ancho_col-2, date_pattern="dd-mm-yyyy")
        ]

    def crear(self):
        """Crea el formulario en la UI"""
        for i, etiqueta in enumerate(self.etiquetas):
            Label(
                self.root,
                text=etiqueta,
                bg=self.color,
                fg="black",
                font=("Segoe UI", 10, "bold")
            ).grid(row=1, column=i, padx=5, pady=(10,2))

        for i, entrada in enumerate(self.entradas):
            entrada.grid(row=2, column=i, padx=20, pady=4, ipadx=3, ipady=3)
    
    def limpiar_formulario(self):
        """Limpia todos los campos del formulario"""
        self.valor_ejercicio.set("")
        self.valor_peso.set(0.0)
        self.valor_reps.set(0.0)
        self.valor_series.set(0.0)
        self.valor_fecha.set("")
