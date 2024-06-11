arquivo = open("/home/bruno/Documentos/Estudos/Programação/aulas-dio-python/03 - Manipulando Arquivos/lorem.txt", "r")

print(arquivo.read()) # Lê o arquivo inteiro
print(arquivo.readline()) # Lê o arquivo linha a linha, sem carregar todo o conteúdo na memória
print(arquivo.readlines()) # Lê todo o conteúdo do arquivo e separa as linhas em uma lista.



#Dica - esse looping verifica se a linha tem conteúdo, enquanto a condição for verdadeira, ele lê a linha. 
#while len(linha := arquivo.readline()):
#    print(linha)

arquivo.close()