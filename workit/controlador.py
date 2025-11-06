"""Script con las funciones para controlar la app"""

import re
from modulo import SqlExecutor

class Controlador():
    """Clase que controla la interacción entre UI y la BBDD"""
    def __init__(self):
        self.executor = SqlExecutor('workouts.db')
        self.executor.crear_tabla_base()
        self.patrones_regex = {
            "letras": r"^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$",
            "numeros":  r"^\d+(\.\d+)?$",
            "fecha": r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
        }

    def validar_registro(self, data):
        """Valida el input mediante expresiones regulares"""
        if not re.match(self.patrones_regex['letras'], str(data['ejercicio'])):
            print("❌ Input inválido para ejercicio, solo se admiten letras")
            return False
        if not re.match(self.patrones_regex['numeros'], str(data['peso'])):
            print("❌ Input inválido para peso, solo se admiten números")
            return False
        if not re.match(self.patrones_regex['numeros'], str(data['reps'])):
            print("❌ Input inválido para reps, solo se admiten números")
            return False
        if not re.match(self.patrones_regex['numeros'], str(data['series'])):
            print("❌ Input inválido para series, solo se admiten números")
            return False
        if not re.match(self.patrones_regex['fecha'], str(data['fecha'])):
            print("❌ Input inválido para fecha, solo se admite formato dd-mm-yyyy")
            return False

        return True

    def agregar_registro(self, data):
        """Añade un registro a la base de datos"""
        self.executor.agregar_bbdd((
            data['ejercicio'],
            data['peso'],
            data['reps'],
            data['series'],
            data['fecha']
        ))
        print("✅ Registro agregado correctamente")

    def borrar_registro(self, id_registro):
        """Elimina un registro de la base de datos"""
        self.executor.borrar_bbdd((id_registro, ))
        print("✅ Registro eliminado correctamente")

    def consultar_registro(self):
        """Consulta los todos los registros de la base de datos"""
        registros = self.executor.consultar_bbdd()
        print("✅ Datos obtenidos correctamente")
        return registros

    def modificar_registr(self, data):
        """Modifica un registro de la base de datos"""
        self.executor.modificar_bbdd((
            data['ejercicio'],
            data['peso'],
            data['reps'],
            data['series'],
            data['fecha'],
            data['id']
        ))
        print("✅ Registro modificado correctamente")
