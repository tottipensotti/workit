"""Log UDP Server"""

import os
import socketserver
from datetime import datetime
from pathlib import Path

HOST = "127.0.0.1"
PORT = 9999

class ServerHandler(socketserver.BaseRequestHandler):
    """Clase para manejar el server UDP"""

    def _obtener_ruta_archivo(self):
        fecha = datetime.now().strftime("%Y%m%d")
        root = Path(__file__).resolve().parent.parent.parent
        return f"{root}/logs/logs_servidor_{fecha}.txt"

    def _escribir_log(self, log):
        file_path = self._obtener_ruta_archivo()
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(log + "\n")

    def handle(self):
        """Método para interactuar con el servidor"""
        raw_data = self.request[0].strip()
        socket = self.request[1]

        try:
            msg = raw_data.decode("utf-8", errors="replace")
        except Exception:
            msg = str(raw_data)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip, port = self.client_address
        log = f"[{timestamp}] [SERVIDOR] {ip}:{port} | {msg}"

        self._escribir_log(log)
        print(log)

        try:
            socket.sendto(bytes([0xA0]), self.client_address)
        except Exception:
            pass

if __name__ == "__main__":
    with socketserver.UDPServer((HOST, PORT), ServerHandler) as server:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [SERVIDOR] | Servidor escuchando en {HOST}:{PORT}")
        server.serve_forever()
