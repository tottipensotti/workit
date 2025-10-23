from tkinter import Tk, Label, StringVar, DoubleVar, Entry, Button, W, E
from tkinter import ttk
from controlador import alta_controlador, borrar_controlador, consultar_controlador, actualizar_treeview

def iniciar_app():

    root = Tk()
    root.title("Tarea POO")

    Label(root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", width=60).grid(row=0, column=0, columnspan=4, sticky=W+E)

    Label(root, text="Producto").grid(row=1, column=0, sticky=W)
    Label(root, text="Cantidad").grid(row=2, column=0, sticky=W)
    Label(root, text="Precio").grid(row=3, column=0, sticky=W)

    a_val, b_val, c_val = StringVar(), DoubleVar(), DoubleVar()
    w_ancho = 20

    Entry(root, textvariable=a_val, width=w_ancho).grid(row=1, column=1)
    Entry(root, textvariable=b_val, width=w_ancho).grid(row=2, column=1)
    Entry(root, textvariable=c_val, width=w_ancho).grid(row=3, column=1)

    tree = ttk.Treeview(root)
    tree["columns"] = ("col1", "col2", "col3")
    tree.column("#0", width=90, anchor=W)
    tree.column("col1", width=200)
    tree.column("col2", width=200)
    tree.column("col3", width=200)
    tree.heading("#0", text="ID")
    tree.heading("col1", text="Producto")
    tree.heading("col2", text="Cantidad")
    tree.heading("col3", text="Precio")
    tree.grid(row=10, column=0, columnspan=4)

    Button(root, text="Alta", command=lambda: alta_controlador(a_val, b_val, c_val, tree)).grid(row=6, column=1)
    Button(root, text="Consultar", command=lambda: consultar_controlador(a_val.get())).grid(row=7, column=1)
    Button(root, text="Borrar", command=lambda: borrar_controlador(tree)).grid(row=8, column=1)

    actualizar_treeview(tree)
    root.mainloop()