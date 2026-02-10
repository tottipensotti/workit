"""Log UDP Server"""

import socketserver
import os
from datetime import datetime

HOST = "127.0.0.1"
PORT = 9999

class ServerHandler(socketserver.BaseRequestHandler):
    """Clase para manejar el server UDP"""

    def _obtener_ruta_archivo(self):
        fecha = datetime.now().strftime("%Y%m%d")
        return f"./logs/logs_servidor_{fecha}.txt"

    def _escribir_log(self, log):
        file_path = self._obtener_ruta_archivo()
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(log + "\n")

    def handle(self):
        """Método para interactuar con el servidor"""
        data = self.request[0].strip()
        socket = self.request[1]

        try:
            msg = data.decode("utf-8", errors="replace")
        except Exception:
            msg = str(data)

        log_ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = f"[{log_ts}] {self.client_address[0]}:{self.client_address[1]} {msg}"
        self._escribir_log(log)

        try:
            socket.sendto(bytes([0xA0]), self.client_address)
        except Exception:
            pass

if __name__ == "__main__":
    with socketserver.UDPServer((HOST, PORT), ServerHandler) as server:
        print(f"Servidor escuchando en {HOST}:{PORT}")
        server.serve_forever()
