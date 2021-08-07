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

 #cria um soquete e define o modo de uso dele como IP e TCP
HOST = 'localhost'
PORT = 5000

meu_servidor= (HOST, PORT)
servidor_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_TCP.bind(meu_servidor) # faz o bind do ip e a porta para que possa comecar a ouvir
servidor_TCP.listen(5)#comeca a ouvir

def receber_cliente(cliente):

    recebido = cliente.recv(2048)

    while recebido!=b' ':
        print("\n")
        print(recebido, ", CLIENTE:" , HOST[1])#Imprime a mensagem enviada pelo cliente
        
        hora = time.ctime()
        hora = hora.split()
        print("\n")
        teclado=input("Digite um código do cliente para o servidor enviar a hora de atendimento : " )


        para_enviar=("Servidor respondeu: " + 
                "Oi cliente " + teclado + ", sua hora de atendimento e: " + hora[3]) 
        cliente.sendto(para_enviar.encode(), dest)
        
        recebido = cliente.recvfrom(2048)
        print (recebido)
        if teclado=="sair":
            cliente.close()
    #fim do socket

while True:
#aceita a conexão com o cliente
    (cliente_soquete_msg_formatada, HOST) = servidor_TCP.accept()
    print("Conexao iniciada com ", HOST,  ".")#Imprime o ip do cliente que conectou
  
    dest=HOST 

    t=threading.Thread(target=receber_cliente,args=(cliente_soquete_msg_formatada,))
    t.start()

