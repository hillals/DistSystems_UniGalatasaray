#!/usr/bin/env python3

import socket
#from sumapi.api import SumAPI
#api = SumAPI(username='GSUINF443', password='wHxuqxdQ95cT')

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12345        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind() is used to associate the socket with a specific network interface and port number:
    s.bind((HOST, PORT))
    # listen() enables a server to accept() connections. It makes it a “listening” socket:
    s.listen()
    # accept() blocks and waits for an incoming connection. 
    # When a client connects, it returns a new socket object representing 
    #       the connection and a tuple holding the address of the client.
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            #api.sentiment_analysis(data, domain='general')
            if not data:
                break
            reply = 'Server Says: ' + data.decode('utf-8')
            conn.sendall(str.encode(reply))

    # If conn.recv() returns an empty bytes object, b'', 
    # then the client closed the connection and the loop is terminated. 

    #The with statement is used with conn to automatically close the socket at the end of the block.