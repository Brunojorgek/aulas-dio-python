def exibir_poema(data_extenso, *args, **kwargs):
	texto = "\n".join(args)
	meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
	mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
	print(mensagem)

exibir_poema("Terça-feira 25 de julho de 2023", # data_extenso
	     
        "Zen of Python", # *args Lista de Tuplas
	    "Beautiful is better than ugly.",
	    "Exlicit is better tha implicit",
    
	     
         autor = "Tim Peters", ano = 1999)# *kwargs - Lista de Dicionários
