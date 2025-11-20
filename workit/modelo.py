"""Clases y funciones para manejar la interacción con la BBDD"""

import sqlite3

class BaseConector():
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

class SqlExecutor(BaseConector):
    """Clase que ejecuta las consultas SQL"""
    def __init__(self, db):
        super().__init__(db)
        self.cursor = self.connection.cursor()

    def consultar_bbdd(self):
        """Realiza una consulta a la base de datos"""
        sql = "SELECT * FROM workouts ORDER BY id ASC"
        try:
            query = self.cursor.execute(sql)
            data = query.fetchall()
            self.connection.commit()
            return data
        except Exception as e:
            print(f"❌ Error al obtener los datos: {e}")
            return None

    def agregar_bbdd(self, data):
        """Agregar un registro a la base de datos"""
        sql = """
            INSERT INTO workouts (ejercicio, peso, reps, series, fecha)
            VALUES (?, ?, ?, ?, ?)
        """
        try:
            self.cursor.execute(sql, data)
            self.connection.commit()
        except Exception as e:
            print(f"❌ Error al agregar registro: {e}")

    def borrar_bbdd(self, data):
        """Borra un registro de la base de datos"""
        sql = "DELETE FROM workouts WHERE id = ?"
        try:
            self.cursor.execute(sql, data)
            self.connection.commit()
        except Exception as e:
            print(f"❌ Error al borrar registro: {e}")

    def modificar_bbdd(self, data):
        """Modifica un registro con nuevos datos"""
        sql = """
            UPDATE workouts
            SET
                ejercicio=?,
                peso=?,
                reps=?,
                series=?,
                fecha=?
            WHERE id=?
            ;
        """
        try:
            self.cursor.execute(sql, data)
            self.connection.commit()
        except Exception as e:
            print(f"❌ Error al modificar registro: {e}")
