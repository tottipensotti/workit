"""Clase BaseConector"""

import sqlite3

class BaseConector:
    """Clase para inicializar la base de datos"""
    def __init__(self, db):
        self.database = db
        self.connection = self.conectar_bbdd()

    def conectar_bbdd(self):
        """Genera la conexión con la base de datos"""
        try:
            conn = sqlite3.connect(self.database)
            print("✅ Conexión exitosa a la base de datos")
            return conn
        except Exception as e:
            print(f"❌ Error al conectar a la base de datos: {e}")
            return None

    def crear_tabla_base(self):
        """Crea la tabla principal de la aplicación"""
        cursor = self.connection.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ejercicio VARCHAR(20) NOT NULL,
                peso REAL,
                reps INTEGER,
                series INTEGER,
                fecha VARCHAR(10)
            )
        """
        try:
            cursor.execute(sql)
            self.connection.commit()
            print("✅ Tabla creada correctamente")
        except Exception as e:
            print(f"❌ Error al crear la tabla:{e}")
