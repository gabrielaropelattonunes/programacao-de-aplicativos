import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor ()

cursor.execute (''' CREATE TABLE IF NOT EXISTS alunos(id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_aluno TEXT NOT NULL,
                    telefone_aluno TEXT,
                    turma_aluno TEXT,
                    idade_aluno INTEGER,
                    cpf_aluno TEXT UNIQUE NOT NULL )''')

nome_aluno = input("digite o nome do aluno: ")
telefone_aluno = input("digite o telefone do aluno: ")
turma_aluno = input("digite a turma do aluno: ")
idade_aluno = int(input("digite a idade do aluno: "))
cpf_aluno = input("digite o cpf inteiro: ")

comando_inserir = (f''' INSERT INTO alunos(nome_aluno,telefone_aluno,turma_aluno,idade_aluno,cpf_aluno)
                         VALUES('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{cpf_aluno}')''')

cursor.execute(comando_inserir)
conexao.commit()
conexao.close()

print("dados foram atualizados!")