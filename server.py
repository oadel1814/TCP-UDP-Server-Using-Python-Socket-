import socket
import threading

PORT = 5050
HEADER = 64
DISCONNECT_MESSAGE = "!DISCONNECTED"
INVALID_MESSAGE = "!INVALID MESSAGE"
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

print(SERVER)


# print(SERVER)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_request(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                response = str(msg[1:-1].strip())
                if (msg[0] == 'A'):
                    response = sorted(response, reverse=True)
                elif (msg[0] == 'C'):
                    response = sorted(response)
                elif (msg[0] == 'D'):
                    response = response.upper()
                else:
                    response = msg[0] + response
                conn.send(str(response).encode(FORMAT))
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(f"[SERVER IS LISTENNING]...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_request, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting.....")
start()