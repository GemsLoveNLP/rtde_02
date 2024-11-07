import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print(f"Host name = {host}")
addr = socket.gethostbyname(host)
print(f"Address = {addr}")
port = 12345

# Bind the socket to a public host and an arbitrary port
server_socket.bind((addr, 12345))
server_socket.listen(1)

print("Server is waiting for a connection...")
conn, addr = server_socket.accept()
print(f"Connected by: {addr}")

while True:
    # Receive data from the client
    data = conn.recv(1024)
    if not data:
        break
    decoded = data.decode()
    print(f"Server: {decoded}")

# Close the connection
conn.close()
