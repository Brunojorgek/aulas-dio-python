from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open("meu_arquivo.py")
except FileExistsError as exc:
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possível abrir arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")


#try:
#    arquivo = open(ROOT_PATH / "novo_diretorio")
#except IsADirectoryError as exc:
#    print(f"Não foi possível abrir arquivo: {exc}")
