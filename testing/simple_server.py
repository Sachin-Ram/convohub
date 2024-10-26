import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = "localhost"
port = 1000

# Bind the socket to the host and port
s.bind((host, port))

# Listen for incoming connections
s.listen(1)
print("Server is listening in {}:{}".format(host, port))

while True:
    # Accept a new client connection
    client, addr = s.accept()
    print("Got a connection from {}".format(addr))

    fulldata = ""

    while True:
        # Receive data from the client
        data = client.recv(1024).decode('utf-8')

        if not data:  # Check if the client has disconnected
            print(f"Client {addr} disconnected.")
            client.close()
            break

        fulldata += data

        # Check if the received data contains a newline character
        if "\n" in data:
            final_data = fulldata.strip()

            # Check if the client wants to exit
            if final_data.lower() == "exit":
                print("Exit message received from client {}. Closing connection.".format(addr))
                client.send("Goodbye!\n".encode('utf-8'))  # Send a goodbye message
                client.close()
                break  # Exit the loop for this client

            else:
                print("Data received from {}: {}".format(addr, final_data))
                client.send("Message received!\n".encode('utf-8'))  # Respond to the client
                fulldata = ""  # Reset for the next message
