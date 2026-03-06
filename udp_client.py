import socket
import random
import string
import time
import sys

PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED"
SERVER = "127.0.1.1" 
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send(msg):
    try:
        message = msg.encode(FORMAT)
        
        client.sendto(message, ADDR)
        
        if msg != DISCONNECT_MESSAGE:
            client.settimeout(2.0) 
            data, server_addr = client.recvfrom(2048)
            print(f"[SERVER RESPONSE] {data.decode(FORMAT)}\n")
            
    except socket.timeout:
        print("\n[ERROR] Server took too long to respond. Packet dropped!\n")
    except Exception as e:
        print(f"\n[ERROR] Network error: {e}")
        sys.exit()

def generate_random_string(length=10):
    first_chars = ['A', 'C', 'D', 'X', 'Z'] 
    start_char = random.choice(first_chars)
    pool_of_characters = string.ascii_letters + string.digits
    rest_of_string = ''.join(random.choice(pool_of_characters) for _ in range(length - 1))
    return start_char + rest_of_string


print("[CLIENT STARTING] Sending UDP packets...\n")

for i in range(5):
    random_msg = generate_random_string(random.randint(8, 15))
    print(f"[CLIENT SENDING] {random_msg}")
    send(random_msg)
    time.sleep(3) 

print("[CLIENT DISCONNECTING]...")
send(DISCONNECT_MESSAGE)