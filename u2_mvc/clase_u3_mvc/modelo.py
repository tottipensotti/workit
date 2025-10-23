import sqlite3
import re
from mis_regex import patron_producto

def conexion():
    return sqlite3.connect("mibase.db")

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto TEXT NOT NULL,
                cantidad REAL,
                precio REAL
            )"""
    cursor.execute(sql)
    con.commit()
    con.close()

# Crear tabla al iniciar
try:
    crear_tabla()
except Exception as e:
    print("Error al crear la tabla:", e)

def alta(producto, cantidad, precio):
    if(re.match(patron_producto, producto)):
        con = conexion()
        cursor = con.cursor()
        data = (producto, cantidad, precio)
        sql = "INSERT INTO productos(producto, cantidad, precio) VALUES (?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        con.close()
        return "Producto agregado correctamente"
    else:
        return "Error de validación"

def borrar_por_id(mi_id):
    con = conexion()
    cursor = con.cursor()
    sql = "DELETE FROM productos WHERE id = ?"
    cursor.execute(sql, (mi_id,))
    con.commit()
    con.close()
    return "Producto eliminado correctamente"

def consultar_todos():
    con = conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM productos ORDER BY id ASC"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    con.close()
    return resultado

def consultar_por_nombre(nombre):
    con = conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM productos WHERE producto LIKE ?"
    cursor.execute(sql, ('%' + nombre + '%',))
    resultado = cursor.fetchall()
    con.close()
    return resultado
