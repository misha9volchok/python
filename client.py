# PROGRAMMER MICHAEL VOLCHOK
#!/usr/bin/env python
# Client
# For more info: https://docs.python.org/2/library/socket.html
from socket import *

HOST = gethostname()  # Get local machine name
PORT = 12345  # Reserve a port for your service.

try:
    with socket() as s:  # Creating a socket object
        s.connect((HOST, PORT))  # Establishing a new connection to a remote machine

        while True:  # Running the program in a loop to receive and send many messages
            site_user_input = input('type URL to trace or exit: ')

            if site_user_input == "exit":
                s.send(site_user_input.encode())  # sending the server the client input exit/ url address

                break  # If the client is interested to exit break the connection
            else:
                s.send(site_user_input.encode())
                # send the url address to server

                print(s.recv(1024).decode('UTF-8'))
                # Getting a message back from the remote machine

        print('Connection closed')
except ConnectionRefusedError:  # Couldn't establish a connection to the remote host
    print("No connection could be made because the target machine refused it")
except ConnectionResetError:  # The established connection was reset by the remote host
    print("An existing connection was forcibly closed by the remote host")
