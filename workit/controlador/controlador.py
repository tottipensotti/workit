"""Script con las funciones para controlar la app"""

from typing import Dict, Any, Optional, List
from workit.modelo.executor import Executor
from workit.modelo.registro import Registro
from workit.utils.decoradores import validar_input, log
from workit.utils.observadores import Sujeto, RegistroConsola, RegistroArchivo, RegistroServidor


class Controlador(Sujeto):
    """Clase que controla la interacción entre UI y la BBDD"""
    def __init__(self) -> None:
        super().__init__()
        self.executor: Executor = Executor()
        self.patrones_regex: Dict[str, str] = {
            "letras": r"^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$",
            "numeros":  r"^\d+(\.\d+)?$",
            "fecha": r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
        }
        self.error_messages: Dict[str, str] = {
            'ejercicio': "Input inválido, solo se admiten letras",
            'peso': "Input inválido, solo se admiten números",
            'reps': "Input inválido, solo se admiten números",
            'series': "Input inválido, solo se admiten números",
            'fecha': "Input inválido, solo se admite formato dd-mm-yyyy"
        }

        # Suscribir observadores
        self.suscribe(RegistroConsola())
        self.suscribe(RegistroArchivo('logs'))
        self.suscribe(RegistroServidor())

    @log("Agregar registro")
    @validar_input
    def agregar_registro(self, data: Dict[str, Any]) -> None:
        """Añade un registro a la base de datos"""
        self.executor.agregar_bbdd(data)

    @log("Eliminar registro")
    def borrar_registro(self, id_registro: int) -> None:
        """Elimina un registro de la base de datos"""
        self.executor.borrar_bbdd(id_registro)

    def consultar_registro(self) -> Optional[List[Registro]]:
        """Consulta los todos los registros de la base de datos"""
        return self.executor.consultar_bbdd()

    @log("Modificar registro")
    @validar_input
    def modificar_registro(self, data: Dict[str, Any]) -> None:
        """Modifica un registro de la base de datos"""
        self.executor.modificar_bbdd(data)
