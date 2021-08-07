import socket
import threading
import time

IP = 'localhost'
PORT = 87

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP,PORT))
server.listen(5)

print("Running on port")

def conection(client_socket):
    request = client_socket.recv(1024)
    print(request)
    print('\n')
    hora = time.ctime()
    hora = hora.split()
    msg = 'Oi cliente, tudo bem? Obrigado pela mensagem. Minha hora eh : '+ hora[3]
    client_socket.send(msg.encode())
    client_socket.close()

while True:
    client, addr = server.accept()
    client_hadler = threading.Thread(target=conection, args=(client,))
    print('Connection accepted')
    client_hadler.start()