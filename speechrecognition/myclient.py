import socket

s=socket.socket()
host="127.0.0.1"
port=12345

s.connect((host,port))
data=str(input())
s.send(data.encode())
print(s.recv(1024).decode())
s.close