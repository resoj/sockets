# =================================================================================================
# Contributing Authors:	    <Anyone who touched the code>
# Email Addresses:          <Your uky.edu email addresses>
# Date:                     <The date the file was last edited>
# Purpose:                  <How this file contributes to the project>
# Misc:                     <Not Required.  Anything else you might want to include>
# =================================================================================================

import socket
import threading

# Handles Received Client 

client_sockets = []

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Recieved data: {data.decode('utf-8')}")

        for client in client_sockets:
            if client != client_socket:
                client.send(data)
    client_socket.close()




    
    #     response = "Server received: " + data.decode('utf-8')
    #     client.socket.send(response.encode('utf-8'))
    # client_socket.close()

host ="10.107.4.230"
port = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(2)

print(f"Server is listening on {host}:{port}")

while True:

    client, addr = server.accept()
    client_sockets.append(client)
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

     


# Use this file to write your server logic
# You will need to support at least two clients
# You will need to keep track of where on the screen (x,y coordinates) each paddle is, the score 
# for each player and where the ball is, and relay that to each client
# I suggest you use the sync variable in pongClient.py to determine how out of sync your two
# clients are and take actions to resync the games