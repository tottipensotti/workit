"""Log Client Server"""

import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 9999

def send(msg):
    """Envia mensaje al servidor"""

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_client.settimeout(1.0)

    try:
        socket_client.sendto(msg.encode("utf-8"), (HOST, PORT))
        try:
            data = socket_client.recvfrom(1024)
            return data
        except socket.timeout:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [CLIENTE] | Timeout: No se recibió ACK del servidor")
            return False
        except Exception as e:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [CLIENTE] | Error al enviar log: {e}")
            return False
    finally:
        try:
            socket_client.close()
        except Exception:
            pass
