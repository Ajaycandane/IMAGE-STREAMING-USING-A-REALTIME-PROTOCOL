import tkinter as tk
from tkinter import filedialog
import socket

def send_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    if not file_path:
        return

    server_address = ('127.0.0.1', 12345)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(server_address)
        with open(file_path, 'rb') as image_file:
            image_data = image_file.read()
        client_socket.sendall(image_data)
        status_label.config(text="Image sent successfully!")

    except Exception as e:
        status_label.config(text=f"Error sending image: {str(e)}")

    finally:
        client_socket.close()

root = tk.Tk()
root.title("Image Transfer Client")

label = tk.Label(root, text="Image Transfer Client")
label.pack(pady=10)

select_button = tk.Button(root, text="Select Image", command=send_image)
select_button.pack()

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
