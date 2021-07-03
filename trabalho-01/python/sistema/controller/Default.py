#grupo:
	#Camila de Souza Ferreira
	#Érica Cristiana dos Santos
	#Gabriel Morais Oliveira
	#Marleison da Silva Rodrigues
	#Tales Félix Gonçalves Cruz
	#Ulisses Xavier Brandão


from ..view.Menu import Menu


import urllib.request #Defines functions and classes which help in opening URLs 
import timeit #Module that measures and calculates the time and execution of programs
from getmac import get_mac_address #From the getmac library that searches for MAC addresses
import socket #Library that allows two processes to communicate
from requests import get #Requests allows sending HTTP requests

class Controller:

    def start(self):
        menu=Menu() 
        option=menu.menuInicial()
        menu.clear()

        if option=="1":

            def connected(): #Function that checks the internet connection
                try:
                    urllib.request.urlopen('http://google.com') #Request URL from google
                    return True 
                except:
                    urllib.request.URLError 
                    return False
            print('You are connected!' if connected() else 'You are not connected!') 
            
        if option=="2":
               
            start = timeit.default_timer() #Sets a default timer, in a platform-specific manner.
            urllib.request.urlopen('http://google.com') 
            end = timeit.default_timer()
            print ('Requisition time: %f' % (end - start))

        if option=="3":
    
            print(f'Local IP: {socket.gethostbyname(socket.gethostname())}') #Function to get the IP address of the local host.

        if option=="4":
     
            print(get_mac_address()) #Get MAC address from device and return it

        if option=="5":

            print(f"Public IP: {get('https://api.ipify.org').text}")  #Function that searches the public IP on this link

        if option=="6":

            print(">>>>>Fim do sistema de Redes 2! Volte sempre!<<<<<<")
            exit()

