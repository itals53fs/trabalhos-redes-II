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
# SOCK_DGRAM cria uma conexão UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    s.bind((HOST, PORT)) # Estabelece o socket a uma porta e um host.

    while True:
        
        data = s.recvfrom(1024) # Recebe dados do cliente.

        if not data:
            break
       
        # Lógica para pegar o horário atual
        horas = time.ctime()
        horas = horas.split()
        horas = horas[3]    
        
        # Estabelecendo a mensagem para envio
        msg = ("Oi cliente, tudo bem? Obrigado pela mensagem. Minha hora é: " + horas)
        
        # Mensagem de retorno da conexão.
        s.sendto(msg.encode('utf-8'), (data[1][0], data[1][1])) # Envia a resposta ao cliente.

        print(data[0].decode('utf-8')) # Imprime a mensagem recebida pelo cliente.  
        print(msg) # Imprime a mensagem enviado para o cliente.  
        break