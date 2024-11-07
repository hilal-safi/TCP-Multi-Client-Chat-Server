# TCP-Multi-Client-Chat-Server

A Python-based TCP server that supports multiple clients in a chat-like environment. Using socket programming and multi-threading, this project enables clients to connect, communicate, and manage sessions in real-time.

## Features

- Multi-Client Support: Clients can connect to the server concurrently, each assigned a unique identifier.
- Session Management: Tracks connection and disconnection times in an in-memory cache.
- Commands:
  - Message: Sends messages to the server, which are echoed back with an acknowledgment.
  - Status: Requests the current status of all active sessions.
  - Exit: Disconnects the client from the server.
  
## Installation

1. Clone the repository:
   ```git clone https://github.com/hilal-safi/tcp-multi-client-chat-server.git```
   
   ```cd tcp-multi-client-chat-server```

3. Requirements: Ensure Python 3.x is installed on your system.

## Usage

1. Start the Server:
   python Server.py

2. Connect Clients:
   In separate terminal windows, start each client:
   python Client.py

3. Client Commands:
   - Type any message to send to the server.
   - Type `status` to view active connections.
   - Type `exit` to disconnect.

## Code Overview

### Server (Server.py)

- Socket Creation: Binds to localhost:12345 using IPv4 and TCP.
- Multi-Threading: Each new client connection spawns a new thread.
- Session Cache: Logs connection and disconnection times for each client.
- Response Logic:
  - Echo: Appends ACK to each received message.
  - Status: Returns session details for active and disconnected clients.
  - Exit: Closes the client connection and logs disconnection time.

### Client (Client.py)

- Connects to the server on localhost:12345.
- Commands:
  - Message: Sends any user input to the server for acknowledgment.
  - Status: Requests the current server session status.
  - Exit: Ends the session with the server.

## Testing

1. Single Client Test: Connect, send messages, request status, and disconnect.
2. Multiple Clients Test: Connect multiple clients and test concurrent interactions.
3. Connection Limits: Adjust the server’s client limit and test exceeding the limit.

## Future Improvements

- GUI: A graphical interface for client interactions.
- Encryption: Secure message transmission with basic encryption.
- Persistent Logging: Store session data in a file or database.
