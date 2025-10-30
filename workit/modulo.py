"""Workit 1.0.0"""

import sqlite3
# pylint: disable=broad-except

def conectar_bbdd() -> sqlite3.Connection | None:
    """Genera una conexión a la base de datos"""
    try:
        conn = sqlite3.connect("mi_base.db")
        print("✅ Conexión exitosa a la base de datos")
        return conn
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None

def crear_tabla_base(conn: sqlite3.Connection) -> None:
    """Crea la tabla principal"""
    cursor = conn.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ejercicio VARCHAR(20) NOT NULL,
            peso_kg REAL,
            reps INTEGER,
            series INTEGER,
            fecha VARCHAR(10)
        )
    """
    try:
        cursor.execute(sql)
        conn.commit()
        print("✅ Tabla creada correctamente")
    except Exception as e:
        print(f"❌ Error al crear la tabla:{e}")

try:
    conexion = conectar_bbdd()
    crear_tabla_base(conexion)
except Exception as e:
    print(f"❌ Ocurrió un error al iniciar el proyecto: {e}")

def consultar(conn: sqlite3.Connection) -> list[any] | None:
    """Realiza una consulta a la base de datos"""
    cursor = conn.cursor()
    sql = "SELECT * FROM workouts ORDER BY id ASC"
    try:
        consulta = cursor.execute(sql)
        data = consulta.fetchall()
        print("✅ Datos obtenidos correctamente")
        return data
    except Exception as e:
        print(f"❌ Error al obtener los datos: {e}")
        return None

def agregar(conn: sqlite3.Connection, datos: tuple[any]) -> None:
    """Agregar un registro a la base de datos"""
    cursor = conn.cursor()
    sql = """
        INSERT INTO workouts
        (ejercicio, peso_kg, reps, series, fecha)
        VALUES(?, ?, ?, ?, ?)
    """
    try:
        cursor.execute(sql, datos)
        conn.commit()
        print("✅ Registro agregado correctamente")
    except Exception as e:
        print(f"❌ Error al agregar registro: {e}")


def borrar(conn: sqlite3.Connection, id_ejercicio: int) -> None:
    """Borra un registro de la base de datos"""
    cursor = conn.cursor()
    data = (id_ejercicio,)
    sql = "DELETE FROM workouts WHERE id = ?"
    try:
        cursor.execute(sql, data)
        conn.commit()
        print("✅ Registro eliminado correctamente")
    except Exception as e:
        print(f"❌ Error al borrar registro: {e}")
