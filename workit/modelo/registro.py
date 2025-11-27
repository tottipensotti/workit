"""Clase Registro"""

from peewee import Model, AutoField, CharField, FloatField, IntegerField
from .conexion import db

class Registro(Model):
    """Clase que representa un registro en la bbdd"""
    id = AutoField()
    ejercicio = CharField(max_length=20)
    peso = FloatField(null=True)
    reps = FloatField(null=True)
    series = IntegerField(null=True)
    fecha = CharField(max_length=10)

    class Meta:
        """Clase de la bbdd"""
        database = db
        table_name = "workouts"
