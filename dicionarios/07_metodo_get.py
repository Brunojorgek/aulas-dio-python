
contatos = {
				"guilherme@gmail.com" : {"nome": "Guilherme", "telefone" : "3333-2221"},
}

contatos["chave"] #Key error

contatos.get("chave") #None
contatos.get("chave", {}) #{}
contatos.get("guilherme@gmail.com", {}) 
#	{"guilherme@gmail.com" : {"nome": "Guilherme", "telefone" : "3333-2221"}