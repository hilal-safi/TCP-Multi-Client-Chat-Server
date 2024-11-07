""" CP372 Programming Assignment
File: Client.py
By: Hilal Safi (190232200), Pranav Baral (210888370)
Date: Oct 2024
Presentation Time: Tuesday, October 29, 2024, 3:40pm

Purpose: Starts the client socket and connects to the server using the TCP protocol.
Asks for input from the client which is passed onto the server.
Outputs the information recieved from the server, including the client name, time, and the message sent.
"""

from socket import *

def start_client():
    # Create a TCP socket object using IPv4 addressing (AF_INET) and TCP (SOCK_STREAM)
    client_socket = socket(AF_INET, SOCK_STREAM)
    
    # Connect to the server running on localhost (127.0.0.1) at port 12345
    client_socket.connect(('localhost', 12345))  # Connect to the server

    # Receive the intro message from the server after connecting
    intro_message = client_socket.recv(1024).decode()
    print(f"Received from server:\n{intro_message}")

    while True:
        message = input("Enter a message to send to the server \nTo close the connection, input 'exit' and to view the server status, input 'status' \nEnter message here: ")
        
        # Send the message to the server (encode it into bytes)
        client_socket.send(message.encode())

        # If the client sends 'exit', receive the exit message before closing the connection
        if message.lower() == "exit":
            # Receive the final message (disconnection message)
            data = client_socket.recv(1024).decode()
            print(f"\nReceived from server:\n{data}")

            # Close the connection after receiving the message
            print("Closing the connection...\n")
            break
        
        # Receive data (up to 1024 bytes) from the server and decode it from bytes to string
        data = client_socket.recv(1024).decode()
        print(f"\nReceived from server:\n{data}")

    client_socket.close()

# This checks if the script is being run directly and starts the client
if __name__ == '__main__':
    start_client()
