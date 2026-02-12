"""Log Client Server"""

import socket
from datetime import datetime
from typing import Tuple, Union

HOST: str = "127.0.0.1"
PORT: int = 9999


def send(msg: str) -> Union[Tuple[bytes, Tuple[str, int]], bool]:
    """Envia mensaje al servidor"""

    socket_client: socket.socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )
    socket_client.settimeout(1.0)

    try:
        socket_client.sendto(msg.encode("utf-8"), (HOST, PORT))
        try:
            data: Tuple[bytes, Tuple[str, int]] = socket_client.recvfrom(1024)
            return data
        except socket.timeout:
            timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(
                f"[{timestamp}] [CLIENTE] | "
                "Timeout: No se recibió ACK del servidor"
            )
            return False
        except Exception as e:
            timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [CLIENTE] | Error al enviar log: {e}")
            return False
    finally:
        try:
            socket_client.close()
        except Exception:
            pass
