import socket
import threading

# NOTE(elsuizo:2022-02-15): usa threading para no tener que esperar cuando se
# envia un mensaje entre un client y el server

# necesitamos un puerto donde conectarnos
# hay consideraciones que se deben tener en cuenta con este numero y no puede
# ser cualquiera(pero casi siempre se usan los mismos)
PORT = 5050
# NOTE(elsuizo:2022-02-15): aca va nuestro IP, podemos poner el numero fijo que
# realmente tenemos o podemos llamar a una funcion de la API para que lo haga
# por nosotros
# SERVER = "192.168.0.195" # este es el inet que nos tira el comando `ifconfig`
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!!!DISCONNECTED"

# NOTE(elsuizo:2022-02-16): aca con esa constante lo que le decimos es que tipo
# de conexion vamos a establecer y vamos a stream la data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# NOTE(elsuizo:2022-02-16): aca "unimos" a el server con la direccion que
# tenemos
server.bind(ADDR)

# NOTE(elsuizo:2022-02-16): con esta funcion vamos a manejar toda la
# comunicacion entre el server y el client
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False

        conn.close()
        print(f"[{addr}] {msg}")

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # NOTE(elsuizo:2022-02-16): en esta linea lo que hacemos es esperar a
        # una nueva conexion al server
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()
