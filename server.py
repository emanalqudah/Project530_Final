import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    
    # Add the client to the list
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"Received from {address}: {message}")

            # Send the message back to the same client
            client_socket.send(message.encode('utf-8'))
        except:
            break

    print(f"Connection from {address} closed")
    clients.remove(client_socket)
    client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {server_address[0]}:{server_address[1]}")

# List to store connected clients
clients = []

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
