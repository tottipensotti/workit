"""Clase SqlExecutor"""

from typing import Dict, List, Any, Optional
from .conexion import db
from .registro import Registro


class Executor:
    """Clase que ejecuta las consultas SQL"""
    def __init__(self) -> None:
        db.connect()
        db.create_tables([Registro])

    def consultar_bbdd(self) -> Optional[List[Registro]]:
        """Realiza una consulta a la base de datos"""
        try:
            return list(Registro.select().order_by(Registro.id.asc()))
        except Exception as e:
            print(f"[ERROR] Error al obtener los datos: {e}")
            return None

    def agregar_bbdd(self, data: Dict[str, Any]) -> None:
        """Agregar un registro a la base de datos"""
        try:
            Registro.create(**data)
        except Exception as e:
            print(f"[ERROR] Error al agregar registro: {e}")

    def borrar_bbdd(self, id_registro: int) -> None:
        """Borra un registro de la base de datos"""
        try:
            registro: Registro = Registro.get_by_id(id_registro)
            registro.delete_instance()
        except Exception as e:
            print(f"[ERROR] Error al borrar registro: {e}")

    def modificar_bbdd(self, data: Dict[str, Any]) -> None:
        """Modifica un registro con nuevos datos"""

        id_registro: str = data.pop("id", None)
        try:
            Registro.update(**data).where(Registro.id == id_registro).execute()
        except Exception as e:
            print(f"[ERROR] Error al modificar registro: {e}")
