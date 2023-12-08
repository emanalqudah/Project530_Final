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

def rot6_client(plaintext_message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    encrypted_message = rotate_text(plaintext_message, 6)
    print(f"Sending encrypted message: {encrypted_message}")
    client_socket.send(encrypted_message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    msg="You cannot sniff me ,I am encrypted !"
    print(msg)
    while True:
    # Get user input and send to the server
   # print(f"Client IP address: {local_ip_address}")
     plaintext_message = input("Enter your message: ")

     rot6_client(plaintext_message)
