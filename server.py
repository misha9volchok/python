# PROGRAMMER MICHAEL VOLCHOK
# !/usr/bin/env python
# Server
# For more info: https://docs.python.org/2/library/socket.html
from socket import *  # Import socket module
from os import system
from file_handler import *
from system_handler import *
from site_handler import *

HOST = gethostname()  # Get local machine name
PORT = 12345  # Reserve a port for your service.

# Opening a firewall port
system(
    'netsh advfirewall firewall add rule name="Open Port {0}" dir=in action=allow protocol=TCP localport={1} remoteip={2}'.format(
        PORT, PORT, HOST))

with socket() as s:  # Create a socket object
    print('Server started!')
    print('Waiting for clients...')

    s.bind((HOST, PORT))  # Bind to the port
    s.listen(5)  # Now wait for client connection.
    c, addr = s.accept()  # Establish connection with client.

    # Remote client machine connection
    print('Got connection from', addr)

    while True:  # Running the program in a loop to receive and send many messages
        # Getting a message from the remote client machine
        """
        The return value is a string representing the data received.
        The maximum amount of data to be received at once 
        is specified by bufsize. 
        """
        remote_input = c.recv(1024).decode('UTF-8')

        if remote_input == "exit":  # if client closes the connection
            print('Connection closed by client')
            c.send("Server connection closed".encode())
            break

        elif site_check(remote_input) == 200:  # if the return code is 200 (valid) trace the address
            new_trace = trace_route(remote_input)
            c.send(new_trace.encode())

            try:
                # create a file and send a status massage to client
                write_to_file(file_path, new_trace)
                c.send("SERVER MASSAGE: The content was appended to the file successfully".encode())

                # Sending our message to the remote client machine as a Byte stream
                """
                For efficient storage of these strings, 
                the sequence of code points are converted into set of bytes.		
                """

            except PermissionError as p:
                c.send("SERVER MASSAGE: You don't have permission to work with the file".encode())
            except FileNotFoundError as f:
                c.send("SERVER MASSAGE: The file doesn't exist on the server".encode())
        else:
            c.send("SERVER MASSAGE: Incorrect input".encode())
