import sqlite3

def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)",(nome,))
    conexao.commit()
    conexao.close()

# o erro é por que foi criado fora do def e não teria como ser executado