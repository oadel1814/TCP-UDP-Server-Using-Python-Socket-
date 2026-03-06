import socket
import threading
import random
import time
import string

PORT = 5050
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    
    client.send(message)

    if msg != DISCONNECT_MESSAGE:
        received_msg = client.recv(2048).decode(FORMAT)
        print(f"[CLIENT SENT] {msg}")
        print(f"[SERVER RESPONSE] {received_msg}\n")

def generate_random_string(length = 10):
    first_chars = ['A', 'C', 'D', 'E', 'F']
    start_char = random.choice(first_chars)

    pool_of_characters = string.ascii_letters + string.digits
    rest_of_string = ''.join(random.choice(pool_of_characters) for _ in range(length - 1))

    return start_char + rest_of_string

print("[CLIENT STARTING] Sending random messages...\n")

for i in range(5):
    random_msg = generate_random_string(random.randint(8, 15))
    send(random_msg)
    time.sleep(3)

print("[CLIENT DISCONNECTING]...")
send(DISCONNECT_MESSAGE)