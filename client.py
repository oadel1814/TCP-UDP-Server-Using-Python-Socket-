import socket
import threading

PORT = 5050
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    print(msg)
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    received_msg = ""
    for c in client.recv(2048).decode(FORMAT):
        received_msg += c
    print(f"[CLIENT RECEIVE] {received_msg}")

print(f"[CLIENT SENDING MESSAGE]... ", end='')
send("COmar")