if ping -q -c 1 www.google.com >log1.txt; then
	echo "✅ Conexão Ativa"
	cat log1.txt
else	
	echo "⛔ Conexão não ativa"
fi