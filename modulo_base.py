import sqlite3

def conectar_bbdd():
    conn = sqlite3.connect("mi_base.db")
    return conn

def crear_tabla_base():
    conn = conectar_bbdd()
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
    cursor.execute(sql)
    conn.commit()

try:
    conectar_bbdd()
    crear_tabla_base()
except Exception as e:
    print(f"Ocurrió un error al iniciar el proyecto: {e}")

def consultar():
    sql = "SELECT * FROM workouts ORDER BY id ASC"
    conn = conectar_bbdd()
    cursor = conn.cursor()
    
    consulta = cursor.execute(sql)
    data = consulta.fetchall()
    
    return data

def agregar(ejercicio, peso, reps, series, fecha):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    data = (ejercicio, peso, reps, series, fecha)
    sql = """
        INSERT INTO workouts
        (ejercicio, peso_kg, reps, series, fecha)
        VALUES(?, ?, ?, ?, ?)
    """
    cursor.execute(sql, data)
    conn.commit()

def borrar(id_ejercicio):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    data = (id_ejercicio,)
    sql = "DELETE FROM workouts WHERE id = ?"
    cursor.execute(sql, data)
    conn.commit()