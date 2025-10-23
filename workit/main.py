"""Workit 1.0.0"""

import re
from tkinter import Label, StringVar, DoubleVar, Entry, Button, W, EW, Tk
from tkinter import ttk
from modulo_base import conectar_bbdd, crear_tabla_base, agregar, consultar, borrar
# pylint: disable=broad-except

CONEXION = conectar_bbdd()


def registrar(ejercicio: str, peso: str, reps: str,
              series: str, fecha: str, mi_treeview: ttk.Treeview) -> None:
    """Añade un registro"""
    cadena = ejercicio
    patron = "^[A-Za-záéíóú]*$"

    print(ejercicio, peso, reps, series, fecha)

    if re.match(patron, cadena):
        print(ejercicio, peso, reps, series, fecha)
        datos = (ejercicio, peso, reps, series, fecha)
        agregar(CONEXION, datos)
        actualizar_vista(mi_treeview)


def borrar_registro(mi_treeview: ttk.Treeview) -> None:
    """Elimina un registro"""
    valor = mi_treeview.selection()
    print(valor)
    item = mi_treeview.item(valor)
    print(item)
    print(item['text'])
    _id = item['text']

    try:
        borrar(CONEXION, _id)
        print("✅ Registro borrado correctamente.")
        tree.delete(valor)
    except Exception as e:
        print(f"❌ Error al eliminar el registro: {e}")


def actualizar_vista(mi_treeview: ttk.Treeview) -> None:
    """Actualizar vista de la GUI"""
    registros = mi_treeview.get_children()
    for elemento in registros:
        mi_treeview.delete(elemento)

    resultado = consultar(CONEXION)
    for fila in resultado:
        print(fila)
        mi_treeview.insert(
            "",
            0,
            text=fila[0],
            values=(fila[1], fila[2], fila[3], fila[4], fila[5])
        )


root = Tk()
root.title("Workit 💪")
root.configure(bg="#f4f4f4")

encabezado = Label(
    root,
    text="Agregue su ejercicio",
    bg="DarkOrchid3",
    fg="thistle1",
    font=("Segoe UI", 12, "bold"),
    height=2,
    width=80,
    anchor="center"
)
encabezado.grid(row=0, column=0, columnspan=10, padx=1, pady=5, sticky=EW)

# Variables
valor_ejercicio = StringVar()
valor_peso = DoubleVar()
valor_reps = DoubleVar()
valor_series = DoubleVar()
valor_fecha = StringVar()
COL_ANCHO = 20

# Etiquetas
etiquetas = [
    "Ejercicio",
    "Peso (kg)",
    "Repeticiones",
    "Series",
    "Fecha (dd-mm-yyyy)"
]

for i, etiqueta in enumerate(etiquetas):
    Label(root, text=etiqueta, bg="#f4f4f4", font=("Segoe UI", 10, "bold")).grid(
        row=1, column=i, padx=5, pady=(10, 2)
    )

# Entradas
entradas = [
    Entry(root, textvariable=valor_ejercicio, width=COL_ANCHO, relief="solid"),
    Entry(root, textvariable=valor_peso, width=COL_ANCHO, relief="solid"),
    Entry(root, textvariable=valor_reps, width=COL_ANCHO, relief="solid"),
    Entry(root, textvariable=valor_series, width=COL_ANCHO, relief="solid"),
    Entry(root, textvariable=valor_fecha, width=COL_ANCHO, relief="solid")
]
for i, entrada in enumerate(entradas):
    entrada.grid(row=2, column=i, padx=20, pady=4, ipadx=3, ipady=3)

# Botones
CONFIG_BOTON = {
    "width": 20,
    "height": 2,
    "relief": "flat",
    "font": ("Segoe UI", 9, "bold"),
    "cursor": "hand2",
    "fg": "black",
    "highlightthickness": 0,
    "bd": 0
}

boton_registro = Button(
    root,
    text="Agregar",
    bg="light green",
    command=lambda: registrar(
        valor_ejercicio.get(),
        valor_reps.get(),
        valor_peso.get(),
        valor_series.get(),
        valor_fecha.get(),
        tree
    ),
    **CONFIG_BOTON
)
boton_registro.grid(row=3, column=0, pady=4, padx=20)

boton_consulta = Button(
    root,
    text="Consultar",
    bg="khaki1",
    command=lambda: consultar(CONEXION),
    **CONFIG_BOTON
)
boton_consulta.grid(row=3, column=1, pady=8)

boton_borrar = Button(
    root,
    text="Borrar",
    bg="light coral",
    command=lambda: borrar_registro(tree),
    **CONFIG_BOTON
)
boton_borrar.grid(row=3, column=2, pady=8)

# Separador encabezados
ttk.Separator(root, orient="horizontal").grid(row=4, column=0, columnspan=10, sticky=W, pady=5)


################################################
#                 TREEVIEW                     #
################################################

columns = ("Id", "Ejercicio", "Peso", "Repeticiones", "Series", "Fecha")
tree = ttk.Treeview(root, show="headings", height=10, columns=columns)

for col in columns:
    tree.heading(col, text=col)

tree.column("Id", width=30, anchor=W)
tree.column("Ejercicio", width=160, anchor=W)
tree.column("Peso", width=100, anchor=W)
tree.column("Repeticiones", width=100, minwidth=80, anchor=W)
tree.column("Series", width=100, minwidth=80, anchor=W)
tree.column("Fecha", width=120, minwidth=80, anchor=W)

tree.grid(row=4, column=0, columnspan=5, padx=20, pady=(10, 20), sticky=EW)

crear_tabla_base(CONEXION)
actualizar_vista(tree)
root.mainloop()
