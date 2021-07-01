echo -e 'Processando...\n'
ifconfig > log3.txt #ifconfig lista as interface de redes, a informação esta sendo direcionada para o arquivo
cat log3.txt | grep inet # cat exibe o arquvo, grep da meth todas linhas que contem 'ether'
echo -e 'Acaso não apareça seu endreço IP acima, ele estarar no log3.txt\n'
exit