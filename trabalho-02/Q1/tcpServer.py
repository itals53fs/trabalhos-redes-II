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
    s.bind((HOST, PORT)) # Estabelece o socket a uma porta e um host.
    s.listen() # Ouve requisições

    conn, addr = s.accept() # Estabelece conexão e endereço
    with conn:

        # Lógica para pegar o horário atual
        horas = time.ctime()
        horas = horas.split()
        horas = horas[3]

        # Estabelecendo a mensagem para envio
        msg = "Oi cliente, tudo bem? Obrigado pela mensagem, Minha hora é: " + horas
        while True:
            data = conn.recv(1024) # Recebe a mensagem do cliente
            if not data:
                break
            print(data.decode('utf-8'))
            print(msg)
            conn.sendall(msg.encode('utf-8'))