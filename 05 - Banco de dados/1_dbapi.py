import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute(
    "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = ("Bruno", "bruno@gmail.com")
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", data)
    conexao.commit()

atualizar_registro(conexao, cursor, "Bruno Jorge", "bruno2@gmail.com", 1)

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?", data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()


def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM cliente WHERE id = ?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")

clente = recuperar_cliente(cursor, 2)
print(cliente)

clientes = listar_clientes(cursor)
for clientes in clientes:
    print(cliente)

# dados = [
#     ("Guilherme", "guilherme@gmail.com"),
#     ("Chappie", "chappie@gmail.com"),
#     ("Melanie", "melanie@gmail.com"),
# ]
# inserir_muitos(conexao, cursor, dados)

