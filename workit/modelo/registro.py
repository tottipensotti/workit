"""Clase Registro"""

from typing import Optional
from peewee import Model, AutoField, CharField, FloatField, IntegerField
from .conexion import db


class Registro(Model):
    """Clase que representa un registro en la bbdd"""
    id: int = AutoField()
    ejercicio: str = CharField(max_length=20)
    peso: Optional[float] = FloatField(null=True)
    reps: Optional[float] = FloatField(null=True)
    series: Optional[int] = IntegerField(null=True)
    fecha: str = CharField(max_length=10)

    class Meta:
        """Clase de la bbdd"""
        database = db
        table_name = "workouts"
