import socket
import base64
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)
local_ip_address = client_socket.getsockname()[0]

while True:
    # Get user input and send to the server
   # print(f"Client IP address: {local_ip_address}")
    message = input("Enter your message: ")
    encode = base64.b64encode(message.encode("utf-8"))
    client_socket.send(message.encode('utf-8'))

    # If you want to receive a response from the server, uncomment the following lines:
    # response = client_socket.recv(1024).decode('utf-8')
    # print(f"Server response: {response}")

# Close the client socket

client_socket.close()
