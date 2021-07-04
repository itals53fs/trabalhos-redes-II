#grupo:
	#Camila de Souza Ferreira
	#Érica Cristiana dos Santos
	#Gabriel Morais Oliveira
	#Marleison da Silva Rodrigues
	#Tales Félix Gonçalves Cruz
	#Ulisses Xavier Brandão

#O site retonar o IP plúblico a requisição get (obter)
wget -qO- http://ipecho.net/plain > log5.txt  #os dados estão sendo direcionados para o arquivo
echo 'Seu ip público é: ' 
cat log5.txt
echo ''
exit