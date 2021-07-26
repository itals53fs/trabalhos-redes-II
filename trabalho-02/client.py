import socket
import time

HOST = 'localhost'
PORT = 87
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
hora = time.ctime()
hora = hora.split()
msg = 'Oi servidor, tudo bem? Minha hora eh: '+ hora[3]
client.send(msg.encode())
response = client.recv(4096)

print(response)