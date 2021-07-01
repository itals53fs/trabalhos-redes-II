echo -e 'Processando...\n' #echo printa mensagens na tela
#traceroute faz uma requisição e aquarda a resposta,
traceroute google.com > log2.txt  # a resposta esta sendo direcionada para log2.txt
cat log2.txt | tail -1 # cat exibe o conteudo do documento, teail -1 pega a ultima linha, onde esta o tempo total
echo -e '\nConfira o log2.txt para ver a resposta completa'
exit