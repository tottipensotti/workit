import re
from tkinter import Label, StringVar, DoubleVar, Entry, Button, W, E, Tk
from tkinter import ttk
from modulo_base import crear_tabla_base, agregar, consultar, borrar


def registrar(ejercicio, peso, reps, series, fecha, tree):
    cadena = ejercicio
    patron = "^[A-Za-záéíóú]*$"

    if re.match(patron, cadena):
        print(ejercicio, peso, reps, series, fecha)
        agregar(ejercicio, peso, reps, series, fecha)
        print("Ejercicio cargado correctamente.")
        actualizar_vista(tree)
    else:
        print("Error en el ejercicio.")


def borrar_registro(tree):
    valor = tree.selection()
    print(valor)
    item = tree.item(valor)
    print(item)
    print(item['text'])
    _id = item['text']

    borrar(_id)
    tree.delete(valor)


def actualizar_vista(mitreeview):
    records = mitreeview.get_children()
    for element in records:
        mitreeview.delete(element)
    
    resultado = consultar()
    for fila in resultado:
        print(fila)
        mitreeview.insert(
            "",
            0,
            text=fila[0],
            values=(fila[1], fila[2], fila[3], fila[4], fila[5])
        )


root = Tk()
root.title("Workout POO")

titulo = Label(root, text="Agregue su ejercicio", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
titulo.grid(row=0, column=0, columnspan=6, padx=1, pady=1, sticky=W+E)

ejercicio = Label(root, text="Ejercicio")
ejercicio.grid(row=1, column=0, sticky=W)
peso = Label(root, text="Peso (KG)")
peso.grid(row=2, column=0, sticky=W)
reps = Label(root, text="Reps")
reps.grid(row=3, column=0, sticky=W)
series = Label(root, text="Series")
series.grid(row=4, column=0, sticky=W)
fecha = Label(root, text="Fecha")
fecha.grid(row=5, column=0, sticky=W)


val_ejercicio, val_peso, val_reps, val_series, val_fecha = StringVar(), DoubleVar(), DoubleVar(), DoubleVar(), StringVar()
ancho_col = 20

entrada_1 = Entry(root, textvariable = val_ejercicio, width = ancho_col)
entrada_1.grid(row=1, column=1)
entrada_2 = Entry(root, textvariable = val_peso, width = ancho_col)
entrada_2.grid(row=2, column=1)
entrada_3 = Entry(root, textvariable = val_reps, width = ancho_col)
entrada_3.grid(row=3, column=1)
entrada_4 = Entry(root, textvariable = val_series, width = ancho_col)
entrada_4.grid(row=4, column=1)
entrada_5 = Entry(root, textvariable = val_fecha, width = ancho_col)
entrada_5.grid(row=5, column=1)

########################
#      TREEVIEW        #
########################

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
tree.column("#0", width=90, minwidth=50, anchor=W)
tree.column("col1", width=200, minwidth=80)
tree.column("col2", width=200, minwidth=80)
tree.column("col3", width=200, minwidth=80)
tree.column("col4", width=200, minwidth=80)
tree.column("col5", width=200, minwidth=80)
tree.heading("#0", text="Id")
tree.heading("col1", text="Ejercicio")
tree.heading("col2", text="Peso (kg)")
tree.heading("col3", text="Repeticiones")
tree.heading("col4", text="Series")
tree.heading("col5", text="Fecha")
tree.grid(row=10, column=0, columnspan=6)

boton_registro = Button(root, text="Agregar Ejercicio", command=lambda:registrar(val_ejercicio.get(), val_reps.get(), val_peso.get(), val_series.get(), val_fecha.get(), tree))
boton_registro.grid(row=6, column=1)

boton_consulta = Button(root, text = "Consultar", command=lambda:consultar())
boton_consulta.grid(row=7, column=1)

boton_borrar = Button(root, text = "Borrar", command=lambda:borrar_registro(tree))
boton_borrar.grid(row=8, column=1)

crear_tabla_base()
actualizar_vista(tree)
root.mainloop()
