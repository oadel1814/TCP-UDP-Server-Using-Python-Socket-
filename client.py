import socket
import threading

PORT = 5050
HEADER = 64
DISCONNECT_MESSAGE = "!DISCONNECTED"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

