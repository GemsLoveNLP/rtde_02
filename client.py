import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("192.168.1.29", 3000))

while True:
    # Get user input
    message = input("Enter message to send to the server: ")
    if message.lower() == 'exit':
        break
    # Send data to the server
    client_socket.sendall(message.encode())

# while Trueclient_socket.sendall("exit".encode())

# Close the connection
client_socket.close()
