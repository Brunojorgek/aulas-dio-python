arquivo = open(
    "/home/bruno/Documentos/Estudos/Programação/aulas-dio-python/03 - Manipulando Arquivos/teste.txt", "w"
    )

arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n escrevendo", "um", "novo", "texto"])
arquivo.close()