"""Log UDP Server"""

import os
import socketserver
from datetime import datetime
from pathlib import Path
from typing import Tuple

HOST: str = "127.0.0.1"
PORT: int = 9999


class ServerHandler(socketserver.BaseRequestHandler):
    """Clase para manejar el server UDP"""

    def _obtener_ruta_archivo(self) -> str:
        fecha: str = datetime.now().strftime("%Y%m%d")
        root: Path = Path(__file__).resolve().parent.parent
        return f"{root}/logs/logs_servidor_{fecha}.txt"

    def _escribir_log(self, log: str) -> None:
        file_path: str = self._obtener_ruta_archivo()
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(log + "\n")

    def handle(self) -> None:
        """Método para interactuar con el servidor"""
        raw_data: bytes = self.request[0]
        socket_client = self.request[1]

        try:
            msg: str = raw_data.decode("utf-8", errors="replace").strip()
        except Exception:
            msg: str = str(raw_data).strip()

        timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip: str
        port: int
        ip, port = self.client_address
        log: str = f"[{timestamp}] [SERVIDOR] {ip}:{port} | {msg}"

        self._escribir_log(log)
        print(log)

        try:
            socket_client.sendto(bytes([0xA0]), self.client_address)
        except Exception:
            pass


if __name__ == "__main__":
    with socketserver.UDPServer((HOST, PORT), ServerHandler) as server:
        ts: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{ts}] [SERVIDOR] | Servidor escuchando en {HOST}:{PORT}")
        server.serve_forever()
