#grupo:
	#Camila de Souza Ferreira
	#Érica Cristiana dos Santos
	#Gabriel Morais Oliveira
	#Marleison da Silva Rodrigues
	#Tales Félix Gonçalves Cruz
	#Ulisses Xavier Brandão


import socket  # importação da biblioteca para realizar a conexão.
import time # importação da biblioteca que proporciona as horas atual.

# declarando servidor e porta
HOST = socket.gethostname() #retorna o nome host do sistema atual sob o qual o interpretador Python é executado.
PORT = 65432 # defenindo uma porta para o servidor

# AF_INET cria conexão IPV4 
# SOCK_STREAM cria uma conexão TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT)) # Estabelece o socket a uma porta e um host.

    # Lógica para pegar o horário atual
    horas = time.ctime()
    horas = horas.split()
    horas = horas[3]

    # Estabelecendo a mensagem para envio
    msg = "Ola servidor, tudo bem? minha hora é: " + horas
    s.sendall(msg.encode('utf-8'))
    data = s.recv(1024)

print("Recebido: ", repr(data.decode('utf-8')))