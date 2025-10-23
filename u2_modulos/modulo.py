import sqlite3
import re

# ##############################################
# MODELO
# ##############################################
 
def conexion():
    con = sqlite3.connect("mibase.db")
    return con

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    
    sql = """CREATE TABLE productos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             producto varchar(20) NOT NULL,
             cantidad real,
             precio real)
    """
    cursor.execute(sql)
    con.commit()

try:
    conexion()
    crear_tabla()
except:
    print("Hay un error")


def alta(producto, cantidad, precio):
 
    print(producto, cantidad, precio)
    con=conexion()
    cursor=con.cursor()
    data=(producto.get(), cantidad.get(), precio.get())
    sql="INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
    cursor.execute(sql, data)
    con.commit()
    return "Estoy en alta todo ok"
 
def consultar(compra):
    
    print(compra)

def borrar(tree):
    valor = tree.selection()
    print(valor)   #('I005',)
    item = tree.item(valor)
    print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
    print(item['text'])
    mi_id = item['text']

    con=conexion()
    cursor=con.cursor()
    #mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM productos WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)


def consulta1(mitreview):

    # CONSULTA A LA BASE
    sql = "SELECT * FROM productos ORDER BY id ASC"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)
    resultado = datos.fetchall()
    return resultado
