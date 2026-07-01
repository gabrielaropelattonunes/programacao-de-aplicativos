import sqlite3

def atualizar_nome_aluno(id_aluno,novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("UPDATE alunos SET nome =? WHERE id_aluno ", (novo_nome,id_aluno))

    conexao.commit()
    conexao.close()

id = int(input("digite o id: "))
novo_id = int(input("digite o novo id: "))
print("novo id atualizado!")

# estava faltando o where pra executar a funçao que pede
# no cursor execute tambem faltava a variavel 
# e os inputs para o nome novo