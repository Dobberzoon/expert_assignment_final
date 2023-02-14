import socket
import sys


def server():
    host = socket.gethostname()
    port = 7000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    connection, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        connection.send(data.encode())
    connection.close()


if __name__ == "__main__":
    server()
