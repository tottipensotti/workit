"""Crea la conexion"""

from pathlib import Path
from peewee import SqliteDatabase

db_path: Path = Path(__file__).parent.parent / "workouts.db"
db: SqliteDatabase = SqliteDatabase(str(db_path))
