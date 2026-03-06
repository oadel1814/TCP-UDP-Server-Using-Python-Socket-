import socket
import threading

PORT = 5050
HEADER = 64
BUFFER_SIZE = 1024
DISCONNECT_MESSAGE = "!DISCONNECTED"
INVALID_MESSAGE = "!INVALID MESSAGE"
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

print(SERVER)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def handle_message(msg_bytes, addr):
    try:
        msg = msg_bytes.decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            print(f"[{addr}] Sent disconnect notification.")
            return

        if len(msg) > 0:
            response = str(msg[1:].strip())
            
            if (msg[0] == 'A'):
                response = "".join(filter(lambda x:x.isalpha(), sorted(response,key=lambda x:x.lower(), reverse=True)))
            elif (msg[0] == 'C'):
                response = "".join(filter(lambda x:x.isalpha(), sorted(response,key=lambda x:x.lower())))
            elif (msg[0] == 'D'):
                response = response.upper()
            else:
                response = msg[0] + response
        else:
            response = INVALID_MESSAGE
            
        server.sendto(str(response).encode(FORMAT), addr)
        print(f"[{addr}] message: {msg}")
        
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred with {addr}: {e}")

def start():
    print(f"[UDP SERVER IS LISTINING] on {SERVER}:{PORT}")

    while True:
        data, addr = server.recvfrom(BUFFER_SIZE)
        thread = threading.Thread(target=handle_message, args=(data, addr))
        thread.start()

print("[STARTING] UDP server is starting.....")
start()