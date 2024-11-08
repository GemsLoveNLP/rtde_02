import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 3000))

while True:
    # Get user input
    # message = "[-240,-189]"
    message = input()
    if message.lower() == 'exit':
        break
    # Send data to the server
    client_socket.sendall(message.encode())

# while Trueclient_socket.sendall("exit".encode())

# Close the connection
client_socket.close()
