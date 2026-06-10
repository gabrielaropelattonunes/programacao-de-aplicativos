import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor ()

cursor.execute (''' create table if not exists alunos(id_aluno integer primary key autoincrement,
                    nome_aluno text not null,
                    telefone_aluno text,
                    turma_aluno text,
                    idade integer,
                    cpf text unique not null )''')

nome_aluno = input("digite o nome do aluno: ")
telefone_aluno = input("digite o telefone do aluno: ")
turma_aluno = input("digite a turma do aluno: ")
idade_aluno = int(input("digite a idade do aluno: "))
cpf_aluno = input("digite o cpf inteiro: ")

comando_inserir = f''' insert into escola_demonstracao (nome,telefone,turma,idade,cpf)
                        values('{nome_aluno}','{telefone_aluno}','{turma_aluno}','{idade_aluno}','{cpf_aluno}')'''

cursor.execute(comando_inserir)
conexao.commit()
conexao.close()

print("dados foram atualizados!")