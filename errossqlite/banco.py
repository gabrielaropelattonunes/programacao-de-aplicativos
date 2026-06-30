import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
            CREAT TABLE IF NOT EXISTS escolas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT 
                   nome TEXT NOT NULL 
                   )
                   ''')
    
    conexao.commit()
    conexao.close()

# não foi criado o banco de dados 
# e não tem o conexao.commit para salvar 
