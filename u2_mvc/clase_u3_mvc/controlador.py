from modelo import alta, borrar_por_id, consultar_todos, consultar_por_nombre

def alta_controlador(producto_var, cantidad_var, precio_var, treeview):
    producto = producto_var.get()
    cantidad = cantidad_var.get()
    precio = precio_var.get()
    resultado = alta(producto, cantidad, precio)
    print(resultado)
    actualizar_treeview(treeview)

def actualizar_treeview(treeview):
    for item in treeview.get_children():
        treeview.delete(item)
    resultados = consultar_todos()
    for fila in resultados:
        treeview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))

def borrar_controlador(treeview):
    seleccion = treeview.selection()
    if seleccion:
        item = treeview.item(seleccion)
        mi_id = item['text']
        resultado = borrar_por_id(mi_id)
        print(resultado)
        treeview.delete(seleccion)

def consultar_controlador(nombre):
    resultados = consultar_por_nombre(nombre)
    for fila in resultados:
        print(fila)
