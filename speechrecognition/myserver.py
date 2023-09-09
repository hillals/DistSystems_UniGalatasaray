import socket
import time
s=socket.socket()
host="127.0.0.1"
port=12345

s.bind((host,port))
s.listen(5)

print("baslıyor yazsın")
connection_socket,addr=s.accept()

while True:
    time.sleep(2)
    data=connection_socket.recv(1024).decode()
    print("got connection from",addr)
    print("says:"+data)
    connection_socket.send(b"basarili thanks for connecting\n")
    

