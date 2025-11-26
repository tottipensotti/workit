"""Clase SqlExecutor"""

from .conexion import BaseConector
from .registro import Registro

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
            return [ Registro.generar(dato) for dato in data ]
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

    def borrar_bbdd(self, id_registro):
        """Borra un registro de la base de datos"""
        sql = "DELETE FROM workouts WHERE id = ?"
        try:
            self.cursor.execute(sql, (id_registro, ))
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
