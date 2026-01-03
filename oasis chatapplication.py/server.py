import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

clients = {}
lock = threading.Lock()

def broadcast(message, sender_socket):
    with lock:
        for client in clients:
            if client != sender_socket:
                client.send(message)

def handle_client(client_socket):
    try:
        username = client_socket.recv(1024).decode('utf-8')
        with lock:
            clients[client_socket] = username

        broadcast(f"{username} joined the chat.\n".encode('utf-8'), client_socket)

        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(f"{username}: ".encode('utf-8') + message, client_socket)

    except:
        pass
    finally:
        with lock:
            username = clients.get(client_socket, "Unknown")
            del clients[client_socket]
        broadcast(f"{username} left the chat.\n".encode('utf-8'), client_socket)
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Chat server started...")

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

start_server()
