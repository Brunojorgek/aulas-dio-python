from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError:
    print("Erro ao abrir arquivo")