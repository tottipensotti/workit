"""Observadores"""

from datetime import datetime
import os
from typing import Dict, List, Any
from abc import ABC, abstractmethod
from workit.server.client import send


class Observador(ABC):
    """Clase constructora de observadores"""
    @abstractmethod
    def update(self, event: Dict[str, Any]) -> None:
        """Actualiza el observador"""


class Sujeto:
    """Clase que notifica a los observadores sobre eventos"""

    def __init__(self) -> None:
        self._observadores: List[Observador] = []

    def suscribe(self, observador: Observador) -> None:
        """Suscribir un nuevo observador"""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def unsuscribe(self, observador: Observador) -> None:
        """Eliminar un nuevo observador"""
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notify(self, event: Dict[str, Any]) -> None:
        """Notificar observadores"""
        for observador in self._observadores:
            observador.update(event)


class RegistroConsola(Observador):
    """
    Observador que registra logs en consola
    """

    def update(self, event: Dict[str, Any]) -> None:
        timestamp = event.get('timestamp', '')
        estado = event.get('status', '')
        mensaje = event.get('message', '')
        datos = event.get('data', '')

        print(f"[{timestamp}] [{estado.upper()}] {mensaje}: {datos}")


class RegistroArchivo(Observador):
    """
    Observador que registra logs en un archivo
    """

    def __init__(self, logs_dir: str) -> None:
        self.logs_dir: str = logs_dir
        os.makedirs(self.logs_dir, exist_ok=True)

    def _obtener_ruta_archivo(self) -> str:
        """
        Genera la ruta del archivo de log
        basado en la fecha actual (formato: logs_YYYYMMDD.txt)
        """
        fecha = datetime.now().strftime("%Y%m%d")
        return f"{self.logs_dir}/logs_{fecha}.txt"

    def update(self, event: Dict[str, Any]) -> None:
        timestamp = event.get('timestamp', '')
        estado = event.get('status', '')
        mensaje = event.get('message', '')
        datos = event.get('data', '')

        log = f"[{timestamp}] [{estado.upper()}] {mensaje}: {datos}\n"

        try:
            file_path = self._obtener_ruta_archivo()
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(log)
        except IOError as e:
            print(f"Error al escribir en archivo de logs: {e}")


class RegistroServidor(Observador):
    """
    Observador que envía logs al servidor UDP
    """

    def update(self, event: Dict[str, Any]) -> None:

        timestamp = event.get('timestamp', '')
        estado = event.get('status', '')
        mensaje = event.get('message', '')
        datos = event.get('data', '')

        msg = f"[{timestamp}] [{estado.upper()}] {mensaje}: {datos}"

        try:
            send(msg)
        except OSError as e:
            print(f"Error al enviar log al servidor: {e}")
