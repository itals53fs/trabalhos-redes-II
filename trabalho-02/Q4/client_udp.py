#grupo:
	#Camila de Souza Ferreira
	#Érica Cristiana dos Santos
	#Gabriel Morais Oliveira
	#Marleison da Silva Rodrigues
	#Tales Félix Gonçalves Cruz
	#Ulisses Xavier Brandão

import socket #Library that allows two processes to communicate
import time

HOST = 'localhost'
PORT = 40000

#cria um soquete e define o modo de uso dele como IP e UDP
cliente_UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
destino = (HOST, PORT) #O par endereco, porta é passado como tupla e armazenado na variavel DESTINO

teclado=""  #Definindo teclado como um objeto do tipo bytes deve ser enviado

while True:
    teclado=input("Digite um número identificador do cliente: \n")# Recebera dados do teclado

    if teclado=="sair":
        break
    #Converte o valor de hora apontado por time para a hora local 
    hora = time.ctime()
    hora = hora.split()
    
    #Envia a mensagem em codificação de caracteres
    msg_formatada=("Saiba o identificador e hora de envio do cliente : " + " IDENTIFICADOR: " + teclado + ", HORA: " + hora[3])
    cliente_UDP.sendto(msg_formatada.encode(),destino)
    recebi=cliente_UDP.recv(2048)#Recebe a resposta do servidor
    print("\n")
    print(recebi) #Imprime a resposta do servidor
    print("\n")
    #fecha a conexão com o servidor
cliente_UDP.close()

