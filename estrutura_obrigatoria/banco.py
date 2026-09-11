import sqlite3

def conectar():
    conexao = sqlite3.connect("gestao_escolar.db")
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao

def inicializar_banco():
    conexao = conectar()
    cursor = conexao.cursor()
    
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS escolas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cidade TEXT NOT NULL
    );
    """)
    
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS turmas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_turma TEXT NOT NULL,
        id_escola INTEGER NOT NULL,
        FOREIGN KEY (id_escola) REFERENCES escolas(id) ON DELETE CASCADE
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        id_turma INTEGER NOT NULL,
        FOREIGN KEY (id_turma) REFERENCES turmas(id) ON DELETE CASCADE
    );
    """)
    
    conexao.commit()
    conexao.close()

inicializar_banco()
print("Banco de dados inicializado com sucesso!")