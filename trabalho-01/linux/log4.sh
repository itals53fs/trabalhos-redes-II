#grupo:
	#Camila de Souza Ferreira
	#Érica Cristiana dos Santos
	#Gabriel Morais Oliveira
	#Marleison da Silva Rodrigues
	#Tales Félix Gonçalves Cruz
	#Ulisses Xavier Brandão


echo 'Processando...'
ifconfig > log4.txt #ifconfig lista as interface de redes, a informação esta sendo direcionada para o arquivo
cat log4.txt | grep ether # cat exibe o arquvo, grep da meth todas linhas que contem 'ether'
echo 'Acaso não apareça seu endreço MAC acima, ele estarar no log4.txt'

exit