"""Crea la conexion"""

from pathlib import Path
from peewee import SqliteDatabase


db_path = Path(__file__).parent.parent / "workouts.db"
db = SqliteDatabase(str(db_path))
