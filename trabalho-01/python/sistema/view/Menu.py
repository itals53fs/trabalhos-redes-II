from os import system #Allows you to run the clear command


class Menu:

    def menuInicial (self): 
        print('''>>>>>Bem vindo ao sistema de Redes 2<<<<<
        1- Verificar se a internet está ativa ou não
        2- Calcular quanto tempo para fazer uma requisição 
        3- Obter informações sobre o IP de seu computador
        4- Obter informações sobre o seu MAC
        5- Obter informações sobre seu IP público (IP do NAT)
        6- Sair''')

        option=input("Digite o número referente a opção escolhida:") #Variable "option" receives value entered by user

        while(option not in ["1","2","3","4","5","6"]): #Repetition structure to ensure that the option entered is 1-6
           option=input("Você digitou uma opção inválida, tente novamente!")
        return option

    def clear(self): #To clear the console screen 
        system("clear")

