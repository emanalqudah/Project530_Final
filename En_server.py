import socket

def rotate_text(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def rot6_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        encrypted_message = client_socket.recv(1024).decode('utf-8')
        print(f"Received encrypted message: {encrypted_message}")

        decrypted_message = rotate_text(encrypted_message, -6)
        print(f"Decrypted message: {decrypted_message}")

        client_socket.close()

if __name__ == "__main__":
    rot6_server()
