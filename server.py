import socket
import os

def save_image(image_data, save_path):
    with open(save_path, 'wb') as image_file:
        image_file.write(image_data)

server_address = ('127.0.0.1', 12345)
save_directory = r'C:\Users\ajayc\Desktop'  # Your specified directory

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_address)

server_socket.listen(1)

print("Server is listening for connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    image_data = b''  # Initialize an empty byte string to hold the image data

    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        image_data += chunk

    filename = f"received_image_{client_address[0]}.jpg"  # Use client's IP address in the filename
    save_path = os.path.join(save_directory, filename)

    save_image(image_data, save_path)

    print("Image received and saved as", save_path)

    client_socket.close()

server_socket.close()
