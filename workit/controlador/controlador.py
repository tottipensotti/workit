"""Script con las funciones para controlar la app"""

import re
from workit.modelo.executor import Executor
from workit.utils.decoradores import validar_input, log
from workit.utils.observadores import Sujeto, RegistroConsola, RegistroArchivo


class Controlador(Sujeto):
    """Clase que controla la interacción entre UI y la BBDD"""
    def __init__(self):
        super().__init__()
        self.executor = Executor()
        self.patrones_regex = {
            "letras": r"^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$",
            "numeros":  r"^\d+(\.\d+)?$",
            "fecha": r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
        }
        self.error_messages = {
            'ejercicio': "Input inválido para ejercicio, solo se admiten letras",
            'peso': "Input inválido para peso, solo se admiten números",
            'reps': "Input inválido para reps, solo se admiten números",
            'series': "Input inválido para series, solo se admiten números",
            'fecha': "Input inválido para fecha, solo se admite formato dd-mm-yyyy"
        }

        # Suscribir observadores
        self.suscribe(RegistroConsola())
        self.suscribe(RegistroArchivo('app.log'))

    @log("Agregar registro")
    @validar_input
    def agregar_registro(self, data):
        """Añade un registro a la base de datos"""
        self.executor.agregar_bbdd(data)

    @log("Eliminar registro")
    def borrar_registro(self, id_registro):
        """Elimina un registro de la base de datos"""
        self.executor.borrar_bbdd(id_registro)

    def consultar_registro(self):
        """Consulta los todos los registros de la base de datos"""
        return self.executor.consultar_bbdd()
    
    @log("Modificar registro")
    @validar_input
    def modificar_registro(self, data):
        """Modifica un registro de la base de datos"""
        self.executor.modificar_bbdd(data)
