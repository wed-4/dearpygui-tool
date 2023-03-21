import os
import shutil
from socket import socket
import threading


def handle_client(client_socket):
    host, port = client_socket.getpeername()
    try:
        while True:
            # Get data from input
            command = input(f"{host}:{port}> ")
            client_socket.send(command.encode())

            # If exit command, break
            if command == "exit":
                break

            # Get response from client
            response = client_socket.recv(1024).decode()
            print(f"Client {host}:{port} responded: {response}")
    except KeyboardInterrupt:
        print("Client shutting down...")
    finally:
        client_socket.close()
        print(f"Client {host}:{port} disconnected")


def start_server(host, port):
    # Create socket
    server = socket()
    server.bind((host, port))

    # Listen for connections
    print("Listening for connections...")
    server.listen(5)

    try:
        while True:
            client, address = server.accept()
            print(f"Received connection from: {address[0]}:{address[1]}")
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server.close()
