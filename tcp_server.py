import socket
import threading

PORT = 5050
HEADER = 64
DISCONNECT_MESSAGE = "!DISCONNECTED"
INVALID_MESSAGE = "!INVALID MESSAGE"
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_request(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    
    try:
        while connected:
            msg_length_str = conn.recv(HEADER).decode(FORMAT)
            
            if not msg_length_str:
                break
                
            msg_length = int(msg_length_str)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr}] Disconnected.")
            else:
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
                    
                conn.send(str(response).encode(FORMAT))
                
            print(f"[{addr}] {msg}")
            
    except ConnectionResetError:
        print(f"[ERROR] Connection with {addr} was lost.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred with {addr}: {e}")
    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr} connection closed. Active connections: {threading.active_count() - 2}")

def start():
    server.listen()
    print(f"[TCP SERVER IS LISTENING] on {SERVER}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_request, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] TCP server is starting.....")
start()