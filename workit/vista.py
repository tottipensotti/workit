"""Script para manejar la vista de la app"""

from tkinter import ttk
from tkinter import Label, StringVar, DoubleVar, Entry, Button, W, EW, Tk
from tkcalendar import DateEntry
from controlador import consultar_registros, borrar_registro, agregar_registro

def actualizar_vista(mi_treeview: ttk.Treeview) -> None:
    """Actualizar vista de la GUI"""
    registros = mi_treeview.get_children()
    for elemento in registros:
        mi_treeview.delete(elemento)

    resultado = consultar_registros()
    for fila in resultado:
        mi_treeview.insert(
            "", "end",
            values=(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
        )

def agregar_vista(ejercicio: str, peso: str, reps: str, series: str, fecha: str, mi_treeview: ttk.Treeview) -> None:
    """Agrega registro y actualiza la vista"""
    try:
        agregar_registro(ejercicio, peso, reps, series, fecha)
        actualizar_vista(mi_treeview)
    except Exception as e:
        print(f"❌ Error al agregar registro: {e}")

def borrar_vista(mi_treeview: ttk.Treeview, id_borrar: str) -> None:
    """Elimina un registro"""
    item = mi_treeview.item(id_borrar).get("values")[0]
    if not item:
        print("⚠️ No se seleccionó ningún registro.")
        return

    try:
        borrar_registro(item)
        actualizar_vista(mi_treeview)
        print("✅ Registro borrado correctamente.")
    except Exception as e:
        print(f"❌ Error al eliminar el registro: {e}")

def inicializar_app():
    """Inicializa y controla la UI de la app"""
    root = Tk()
    root.title("Workit 💪")
    root.configure(bg="#f4f4f4")

    for col in range(5):
        root.columnconfigure(col, weight=1)
    root.rowconfigure(5, weight=1)

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
    encabezado.grid(row=0, column=0, columnspan=5, padx=1, pady=5, sticky=EW)

    # Variables
    valor_ejercicio = StringVar()
    valor_peso = DoubleVar()
    valor_reps = DoubleVar()
    valor_series = DoubleVar()
    valor_fecha = StringVar()
    ancho_col = 20

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
        Entry(root, textvariable=valor_ejercicio, width=ancho_col, relief="solid"),
        Entry(root, textvariable=valor_peso, width=ancho_col, relief="solid"),
        Entry(root, textvariable=valor_reps, width=ancho_col, relief="solid"),
        Entry(root, textvariable=valor_series, width=ancho_col, relief="solid"),
        DateEntry(root, textvariable=valor_fecha, width=ancho_col-2, date_pattern="dd-mm-yyyy"),
    ]
    for i, entrada in enumerate(entradas):
        entrada.grid(row=2, column=i, padx=20, pady=4, ipadx=3, ipady=3)

    # Botones
    config_btn = {
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
        command=lambda: agregar_vista(
            valor_ejercicio.get(),
            valor_peso.get(),
            valor_reps.get(),
            valor_series.get(),
            valor_fecha.get(),
            tree
        ),
        **config_btn
    )
    boton_registro.grid(row=3, column=0, pady=4, padx=20)

    boton_consulta = Button(
        root,
        text="Consultar",
        bg="khaki1",
        command=lambda: consultar_registros,
        **config_btn
    )
    boton_consulta.grid(row=3, column=1, pady=8)

    boton_borrar = Button(
        root,
        text="Borrar",
        bg="light coral",
        command=lambda: borrar_vista(tree, tree.focus()),
        **config_btn
    )
    boton_borrar.grid(row=3, column=2, pady=8)

    # Separador encabezados
    ttk.Separator(root, orient="horizontal").grid(
        row=4,
        column=0,
        columnspan=5,
        sticky=EW,
        pady=5
    )


    ################################################
    #                 TREEVIEW                     #
    ################################################

    columns = ("#", "Ejercicio", "Peso (kg)", "Repeticiones", "Series", "Fecha")
    tree = ttk.Treeview(root, show="headings", height=10, columns=columns)

    for col in columns:
        tree.heading(col, text=col)

    tree.column("#", width=30, anchor=W)
    tree.column("Ejercicio", width=160, anchor=W)
    tree.column("Peso (kg)", width=100, anchor=W)
    tree.column("Repeticiones", width=100, minwidth=80, anchor=W)
    tree.column("Series", width=100, minwidth=80, anchor=W)
    tree.column("Fecha", width=120, minwidth=80, anchor=W)

    tree.grid(row=5, column=0, columnspan=5, padx=20, pady=(10, 20), sticky=EW)

    actualizar_vista(tree)
    root.mainloop()
