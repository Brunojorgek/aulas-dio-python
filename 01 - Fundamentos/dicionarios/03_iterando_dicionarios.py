
contatos = {
			"guilherme@gmail.com" : {"nome": "Guilherme", "telefone" : "3333-2221"},
			"giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "3443-2121"},
			"chappie@gmail.com" : {"nome": "Chapie", "telefone": "3444-9871"},
			"melaine@gmail.com" : {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos: 
	print(chave, contatos[chave])

for chave, valor in contatos.itens():
	print(chave, valor)

#"guilherme@gmail.com" : {"nome": "Guilherme", "telefone" : "3333-2221"},
#"giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "3443-2121"},
#"chappie@gmail.com" : {"nome": "Chapie", "telefone": "3444-9871"},
#"melaine@gmail.com" : {"nome": "Melaine", "telefone": "3333-7766"},