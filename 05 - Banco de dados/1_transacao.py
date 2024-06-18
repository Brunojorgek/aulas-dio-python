import sqlite3
from pathlib import Path

ROOTH_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOTH_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execte("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 2", "teste2@gmail.com"))
    conexao.commit()
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, "Teste3", "teste3@gmail.com"))
    conexao.commit()
except Exception as exc:
    print(f"Ops! um ocorreu! {exc}")