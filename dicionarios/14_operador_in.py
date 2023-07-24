
contatos = {
			"guilherme@gmail.com" : {"nome": "Guilherme", "telefone" : "3333-2221"},
			"giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "3443-2121"},
			"chappie@gmail.com" : {"nome": "Chapie", "telefone": "3444-9871"},
			"melaine@gmail.com" : {"nome": "Melaine", "telefone": "3333-7766"},
}

"guilherme@gmail.com" in contatos #True
"melissa@gmail.com" in contatos #False
"idade" in contatos["guilherme@gmail.com"] #False
"telefone" in contatos["giovanna@gmail.com"] #True