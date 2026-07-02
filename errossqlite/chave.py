import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    conexao.execute("PRAGMA foreign_keys = ON;")
    cursor = conexao.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS turmas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome_turma TEXT,
                   id_serie INTEGER,
                   FOREING KEY (id_series) REFERENCES series(id)
                   )
                   ''')
    conexao.commit()
    conexao.close()

criar_tabela_turma()

# faltava o codigo da foreing key para ser executado certo 
# definir o que é o id 