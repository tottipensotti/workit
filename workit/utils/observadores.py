"""Observadores"""

from datetime import datetime
import os


class Sujeto:
    """Clase que notifica a los observadores sobre eventos"""

    def __init__(self):
        self._observadores = []

    def suscribe(self, observador):
        """Suscribir un nuevo observador"""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def unsuscribe(self, observador):
        """Eliminar un nuevo observador"""
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notify(self, evento):
        """Notificar observadores"""
        for observador in self._observadores:
            observador.update(evento)


class Observador:
    """Clase constructora de observadores"""
    def update(self, event):
        """Actualiza el observador"""
        raise NotImplementedError("Los observadores deben implementar el método update().")

class RegistroConsola(Observador):
    """
    Observador que registra logs en consola
    """

    def update(self, event):
        timestamp = event.get('timestamp', '')
        estado = event.get('status', '')
        mensaje = event.get('message', '')
        datos = event.get('data', None)

        sufijo = f"({datos})" if datos is not None else ""
        print(f"[{timestamp}] [{estado.upper()}] {mensaje}{sufijo}")

class RegistroArchivo(Observador):
    """
    Observador que registra logs en un archivo
    """

    def __init__(self, logs_dir="."):
        self.logs_dir = logs_dir
        os.makedirs(self.logs_dir, exist_ok=True)

    def _obtener_ruta_archivo(self):
        """
        Genera la ruta del archivo de log
        basado en la fecha actual (formato: logs_YYYYMMDD.txt)
        """
        fecha = datetime.now().strftime("%Y%m%d")
        return f"{self.logs_dir}/logs_{fecha}.txt"

    def update(self, event):
        timestamp = event.get('timestamp', '')
        estado = event.get('status', '')
        mensaje = event.get('message', '')
        datos = event.get('data', None)

        sufijo = f": {datos}" if datos is not None else ""
        log = f"[{timestamp}] [{estado.upper()}] {mensaje}{sufijo}\n"

        try:
            file_path = self._obtener_ruta_archivo()
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(log)
        except IOError as e:
            print(f"Error al escribir en archivo de logs: {e}")
