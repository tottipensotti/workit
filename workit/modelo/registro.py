"""Clase Registro"""

class Registro:
    """Representa un registro de la bbdd"""
    def __init__(self, id, ejercicio, peso, reps, series, fecha):
        self.id = id
        self.ejercicio = ejercicio
        self.peso = peso
        self.reps = reps
        self.series = series
        self.fecha = fecha

    @staticmethod
    def generar(data):
        """Genera un registro a partir de una tupla."""
        return Registro(
            id=data[0],
            ejercicio=data[1],
            peso=data[2],
            reps=data[3],
            series=data[4],
            fecha=data[5],
        )
