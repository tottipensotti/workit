"""Crea la conexion"""

from peewee import SqliteDatabase

db = SqliteDatabase("workouts.db")
