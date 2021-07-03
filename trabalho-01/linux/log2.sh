#grupo:
	#Camila de Souza Ferreira
	#Érica Cristiana dos Santos
	#Gabriel Morais Oliveira
	#Marleison da Silva Rodrigues
	#Tales Félix Gonçalves Cruz
	#Ulisses Xavier Brandão


echo -e 'Processando...\n' #echo printa mensagens na tela
#traceroute faz uma requisição e aquarda a resposta,
traceroute google.com > log2.txt  # a resposta esta sendo direcionada para log2.txt
cat log2.txt | tail -1 # cat exibe o conteudo do documento, teail -1 pega a ultima linha, onde esta o tempo total
echo -e '\nConfira o log2.txt para ver a resposta completa'
exit