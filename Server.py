""" CP372 Programming Assignment
File: Server.py
By: Hilal Safi (190232200), Pranav Baral (210888370)
Date: Oct 2024
Presentation Time: Tuesday, October 29, 2024, 3:40pm

Purpose: Starts the server using localhost and port 12345, and the TCP protocol. 
Uses Treading to manage multiple client connections together.
Outputs the client name and time of connection, disconnection and request of input.
Encodes and reads the clients request (through command line input). Will provide status and exit if requested, 
Otherwise outputs the uppercase input with ACK and the time.
"""

import threading
import datetime
from socket import *

# Dictionary to store client connection details (cache)
client_cache = {}

# Counter for client names
client_number = 1

# Uses multi-threading to handle multiple connections and store client features
def handle_client(client_socket, client_name):

    connection_time = datetime.datetime.now()
    client_cache[client_name] = {'connection': connection_time, 'disconnection': None}

    # Sends introductory message after client connects
    intro_message = f"\nYou have connected to the server at {connection_time}. Welcome {client_name}!\n"
    client_socket.send(intro_message.encode())

    # Handle the client communication
    while True:

        data = client_socket.recv(1024).decode()

        # If unable to 3 way handshake, or no data then close connection
        if not data:
            break

        print(f"Received from {client_name}: {data}\n")

        # Allows for connection to close when client inputs 'exit'
        if data.lower() == "exit":
            print(f"{client_name} disconnected")

            # Get the datetime of when the connection was finished.
            client_cache[client_name]['disconnection'] = datetime.datetime.now()

            # Create a message with the disconnection time
            disconnect_time = client_cache[client_name]['disconnection']
            disconnect_message = f"You have ended the connection.\nDisconnect time: {disconnect_time}\n"
            
            # Send the message to the client
            client_socket.send(disconnect_message.encode())

            # Close the socket after sending the final message
            client_socket.shutdown(SHUT_WR)  # Shutdown the writing end to ensure the client receives the message
            client_socket.close()
            break

        # Provide server cache if the user inputs status
        elif data.lower() == "status":

            # Respond with the server cache
            status_msg = f"Server Cache: {client_cache}\n"
            client_socket.send(status_msg.encode())

        # Send the input back
        else:
            # Create a formatted string with the client name and request time
            request_time = datetime.datetime.now()
            header_text = f"Client Name: {client_name}\nRequest Time: {request_time}\n"
            
            upcased_data = header_text + "Message (echoed back): " + data + " ACK\n"
            
            # Send the formatted data back to the client
            client_socket.send(upcased_data.encode())

    client_socket.close()

def start_server():

    global client_number  # Make the client_number global so we can increment it

    # Create a TCP socket object using IPv4 addressing (AF_INET) and TCP (SOCK_STREAM)
    server_socket = socket(AF_INET, SOCK_STREAM)
    
    # Bind the server socket to localhost (127.0.0.1) at port 12345
    server_socket.bind(('localhost', 12345))
    
    # Start listening for incoming connections (backlog of 3 connections)
    server_socket.listen(3)
    print("Server is listening...\n")

    # Infinite loop to keep the server running and accepting connections
    while True:

        # Accept an incoming connection and get the client socket and address
        client_socket, addr = server_socket.accept()

        # Name the client and increment the number for more connections
        client_name = f"Client{client_number:02d}"
        client_number += 1
        print(f"Connection from {addr}, assigned name: {client_name}\n")

        # Use a thread to handle each client connection
        client_thread = threading.Thread(target = handle_client, args = (client_socket, client_name))
        client_thread.start()

# This checks if the script is being run directly and starts the server
if __name__ == '__main__':
    start_server()
