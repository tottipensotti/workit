"""Script con métodos utilizados en la aplicación"""

import sqlite3
import re

# ##############################################
# MODELO
# ##############################################

def conexion():
    """Realiza la conexión a la base de datos"""
    conn = sqlite3.connect("mibase.db")
    return conn

def crear_tabla():
    """Crea una tabla en la base de datos"""
    conn = conexion()
    cursor = conn.cursor()
    sql = """CREATE TABLE productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto varchar(20) NOT NULL,
            cantidad real,
            precio real
        )
    """
    cursor.execute(sql)
    conn.commit()

try:
    conexion()
    crear_tabla()
except Exception as e:
    print(f"Hay un error: {e}")

def alta(producto, cantidad, precio, tree):
    """Realiza la alta de un producto"""
    cadena = producto
    patron="^[A-Za-záéíóú]*$"  #regex para el campo cadena

    if re.match(patron, cadena):
        print(producto, cantidad, precio)
        conn = conexion()
        cursor = conn.cursor()
        data = (producto, cantidad, precio)
        sql = "INSERT INTO productos (producto, cantidad,precio) VALUES (?, ?, ?)"
        cursor.execute(sql, data)
        conn.commit()
        print("Estoy en alta todo ok")
        actualizar_treeview(tree)
    else:
        print("Error en campo producto")

def consultar():
    """Consulta un producto en la base de datos"""
    global compra
    print(compra)

def borrar(tree):
    """Borra un producto de la base de datos"""
    valor = tree.selection()
    print(valor)
    item = tree.item(valor)
    print(item)
    print(item['text'])
    mi_id = item['text']

    conn = conexion()
    cursor = conn.cursor()
    data = (mi_id,)
    sql = "DELETE FROM productos WHERE id = ?;"
    cursor.execute(sql, data)
    conn.commit()
    tree.delete(valor)

def actualizar_treeview(mitreeview):
    """Actualiza la vista de la aplicación"""
    records = mitreeview.get_children()
    for element in records:
        mitreeview.delete(element)

    sql = "SELECT * FROM productos ORDER BY id ASC"
    conn = conexion()
    cursor = conn.cursor()
    datos = cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mitreeview.insert(
            "", 0,
            text=fila[0],
            values=(fila[1], fila[2], fila[3])
        )
