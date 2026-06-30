import sqlite3

def criar_tabela ():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor ()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS escolas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT 
                   )
                   ''')


    cursor.execute('''
                   CREAT TABLE IF NOT EXISTS series (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome_serie TEXT,
                   id_escola INTEGER,
                   FOREIGN KEY (id_escola) REFERENCES escolas(id)
                   )
                   ''')
    

    conexao.commit()
    conexao.close()

# o REFERENCES puxa uma referencia de uma tabela onde a tabela esta limpa entao nao tem o id 