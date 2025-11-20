"""Script para manejar la interacción con la UI de la app"""

from tkinter import ttk
from tkinter import Label, StringVar, DoubleVar, Entry, Button, W, EW, Tk, messagebox
from tkcalendar import DateEntry
from controlador import Controlador

class TkTree():
    """Clase padre con configuración de Tkinter"""
    def __init__(self):
        self.root = Tk()

class Boton:
    """Clase auxiliar para crear botones"""
    def __init__(self, root, texto, bg_color, comando):
        self.root = root
        self.texto = texto
        self.color = bg_color
        self.comando = comando
        self.config_base = {
            "width": 20,
            "height": 2,
            "relief": "flat",
            "font": ("Segoe UI", 9, "bold"),
            "cursor": "hand2",
            "fg": "black",
            "highlightthickness": 0,
            "bd": 0
        }
        self.boton = Button(
            self.root,
            text=self.texto,
            bg=self.color,
            command=self.comando,
            **self.config_base
        )

    def mostrar(self, row, column, **kwargs):
        """Muestra el botón en la grilla"""
        self.boton.grid(row=row, column=column, **kwargs)

class App(TkTree):
    """Clase que maneja la UI"""
    def __init__(self, title):
        super().__init__()
        self.controlador_vista = Controlador()
        self.title = title
        self.header = Label(
            self.root,
            text="Agregue su ejercicio",
            bg="DarkOrchid3",
            fg="thistle1",
            font=("Segoe UI", 12, "bold"),
            height=2,
            width=80,
            anchor="center"
        )
        self.bg_color = "#f4f4f4"
        self.labels = ["Ejercicio", "Peso (kg)", "Repeticiones", "Series", "Fecha"]
        self.columns = ("#", "Ejercicio", "Peso (kg)", "Repeticiones", "Series", "Fecha")
        self.tree = ttk.Treeview(self.root, show="headings", height=10, columns=self.columns)
        self.valor_ejercicio = StringVar()
        self.valor_peso = DoubleVar()
        self.valor_reps = DoubleVar()
        self.valor_series = DoubleVar()
        self.valor_fecha = StringVar()
        self.ancho_col = 20
        self.entries = [
            Entry(self.root, textvariable=self.valor_ejercicio, width=self.ancho_col, relief="solid"),
            Entry(self.root, textvariable=self.valor_peso, width=self.ancho_col, relief="solid"),
            Entry(self.root, textvariable=self.valor_reps, width=self.ancho_col, relief="solid"),
            Entry(self.root, textvariable=self.valor_series, width=self.ancho_col, relief="solid"),
            DateEntry(self.root, textvariable=self.valor_fecha, width=self.ancho_col-2, date_pattern="dd-mm-yyyy"),
        ]
        self.boton_agregar = Boton(
            self.root,
            texto="Agregar",
            bg_color="light green",
            comando=lambda: self.agregar_vista({
                    "ejercicio": self.valor_ejercicio.get(),
                    "peso": self.valor_peso.get(),
                    "reps": self.valor_reps.get(),
                    "series": self.valor_series.get(),
                    "fecha": self.valor_fecha.get()
                })
        )
        self.boton_consultar = Boton(
            self.root,
            texto="Consultar",
            bg_color="khaki1",
            comando=self.controlador_vista.consultar_registro()
        )
        self.boton_borrar = Boton(
            self.root,
            texto="Borrar",
            bg_color="light coral",
            comando=lambda: self.borrar_vista(self.tree.focus())
        )

    def _generar_etiquetas(self):
        """Genera las etiquetas en la UI"""
        for i, etiqueta in enumerate(self.labels):
            Label(
                self.root, text=etiqueta, bg=self.bg_color, font=("Segoe UI", 10, "bold")
            ).grid(row=1, column=i, padx=5, pady=(10,2))

    def _generar_entradas(self):
        """Genera las entradas en la UI"""
        for i, entrada in enumerate(self.entries):
            entrada.grid(row=2, column=i, padx=20, pady=4, ipadx=3, ipady=3)

    def _generar_botones(self):
        """Genero los botones de la UI"""
        self.boton_agregar.mostrar(row=3, column=0, pady=8)
        self.boton_consultar.mostrar(row=3, column=1, pady=8)
        self.boton_borrar.mostrar(row=3, column=2, pady=8)

    def actualizar_vista(self):
        """Actualiza la vista de la UI"""
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)

        resultado = self.controlador_vista.consultar_registro()
        for fila in resultado:
            self.tree.insert(
                "", "end",
                values=(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            )

    def agregar_vista(self, data):
        """Agrega un registro a la UI"""
        try:
            self.controlador_vista.agregar_registro(data)
            self.actualizar_vista()
        except Exception as e:
            print(f"❌ Error al agregar registro: {e}")

    def borrar_vista(self, id_borrar):
        """Elimina un registro de la UI"""
        item = self.tree.item(id_borrar).get('values')[0]
        if not item:
            print("⚠️ No se seleccionó ningún registro.")
            return

        confirmacion = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Estás seguro de eliminar el registro con ID {item}?"
        )

        if not confirmacion:
            print("⚠️ Eliminación cancelada por el usuario.")
            return

        try:
            self.controlador_vista.borrar_registro(item)
            self.actualizar_vista()
        except Exception as e:
            print(f"❌ Error al eliminar el registro: {e}")

    def inicializar_app(self):
        """Inicializa y controla la UI de la app"""
        self.root.title(self.title)
        self.root.configure(bg=self.bg_color)

        for col in range(5):
            self.root.columnconfigure(col, weight=1)
        self.root.rowconfigure(5, weight=1)

        self.header.grid(row=0, column=0, columnspan=5, padx=1, pady=5, sticky=EW)

        self._generar_etiquetas()
        self._generar_entradas()
        self._generar_botones()

        for col in self.columns:
            self.tree.heading(col, text=col)

        self.tree.column("#", width=30, anchor=W)
        self.tree.column("Ejercicio", width=160, anchor=W)
        self.tree.column("Peso (kg)", width=100, anchor=W)
        self.tree.column("Repeticiones", width=100, minwidth=80, anchor=W)
        self.tree.column("Series", width=100, minwidth=80, anchor=W)
        self.tree.column("Fecha", width=120, minwidth=80, anchor=W)

        self.tree.grid(row=5, column=0, columnspan=5, padx=20, pady=(10, 20), sticky=EW)

        self.actualizar_vista()
        self.root.mainloop()
