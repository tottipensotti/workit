"""Log Client Server"""

import socket

HOST = "127.0.0.1"
PORT = 9999

def send(msg):
    """Envia mensaje al servidor"""

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_client.settimeout(1.0)

    try:
        socket_client.sendto(msg.encode("utf-8"), (HOST, PORT))
        try:
            data, _ = socket_client.recvfrom(1024)
            return data
        except Exception as e:
            print(f"Error al recibir ACK: {e}")
            return ""
    finally:
        try:
            socket_client.close()
        except Exception:
            pass

if __name__ == "__main__":
    ACK = send("Test log")
    print("ACK recibido: ", ACK)
