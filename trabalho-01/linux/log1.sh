#grupo:
	#Camila de Souza Ferreira
	#Érica Cristiana dos Santos
	#Gabriel Morais Oliveira
	#Marleison da Silva Rodrigues
	#Tales Félix Gonçalves Cruz
	#Ulisses Xavier Brandão

# ping faz u,ma requisição no endereço do google
# -q sai da requisição -c 1 deixa fazer apenas uma requisição
# A resposta está sendo direcionada para arquivo
if ping -q -c 1 www.google.com >log1.txt; then 
	echo "✅ Conexão Ativa"
	cat log1.txt #cat exibe o conteudo
else	
	echo "⛔ Conexão não ativa"
fi