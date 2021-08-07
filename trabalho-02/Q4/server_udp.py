#grupo:
	#Camila de Souza Ferreira
	#Érica Cristiana dos Santos
	#Gabriel Morais Oliveira
	#Marleison da Silva Rodrigues
	#Tales Félix Gonçalves Cruz
	#Ulisses Xavier Brandão

import socket #Library that allows two processes to communicate
import threading
import time

def receber_cliente(client):  #Função que recebe os clientes

        hora = time.ctime()
        hora = hora.split()
        print("\n")
        teclado=input("Digite o código do cliente para o servidor enviar a hora de atendimento : " )

        para_enviar=("Servidor respondeu: " + 
                "Oi cliente " + teclado + ", sua hora de atendimento e: " + hora[3]) 
   
        servidor_UDP.sendto(para_enviar.encode(), dest)
        recebido = servidor_UDP.recv(2048)
        print("\n")
        print (recebido)

        if teclado=="sair":
            servidor_UDP.close()

 #cria um soquete e define o modo de uso dele como IP e UDP
HOST = 'localhost'
PORT = 40000

servidor_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
meu_servidor= (HOST, PORT)
servidor_UDP.bind(meu_servidor) # faz o bind do ip e a porta para que possa comecar a ouvir

while True:
#aceita a conexão com o cliente
    (cliente_soquete_msg_formatada, HOST) = servidor_UDP.recvfrom(1024)
    print("Conexao iniciada com ", HOST,  " .")#Imprime o ip do cliente que conectou
    print (cliente_soquete_msg_formatada, ", CLIENTE:" , HOST[1])

    dest=HOST
    
    t=t=threading.Thread(target=receber_cliente,args=(cliente_soquete_msg_formatada,)) #Threading para receber multiplos clientes
    t.start() 
    
