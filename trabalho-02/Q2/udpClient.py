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

    # Lógica para pegar o horário atual
    horas = time.ctime()
    horas = horas.split()
    horas = horas[3] 
    
    # Estabelecendo a mensagem para envio
    msg = ("Oi servidor, tudo bem? Minha hora é: " + horas)
    s.sendto(msg.encode('utf-8'), (HOST, PORT)) # Enviando mensagem para o servidor.
    data, addr = s.recvfrom(1024) # Recebendo mensagem

print(data.decode('utf-8')) # Imprime os dados envaidos pelo servidor.