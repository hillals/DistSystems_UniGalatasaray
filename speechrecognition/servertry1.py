import socket
from sumapi.api import SumAPI

s=socket.socket()
host="127.0.0.1"
port=12345
s.bind((host,port))
s.listen(0)

api = SumAPI(username='GSUINF236', password='RPXfvP2yU7v4')

print("sunucu calismaya basliyor")
while True:
    conn, addr = s.accept()
    print("a new client has connected:",addr)
    print("write a sentence")
    sensen=conn.recv(1024).decode()
    analysis=api.sentiment_analysis(sensen, domain='general')
    analysis2=analysis['evaluation']
    analysis3=analysis2['label']
    conn.send(analysis3.encode())









