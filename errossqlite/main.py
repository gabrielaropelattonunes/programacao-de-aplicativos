import sqlite3

def listar_alunos_e_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas ON alunos.id_turma = turmas.id")

    for linha in cursor.fetchall():
        print(f"aluno: {linha [0]}| turma: {linha[1]}")
    conexao.close()

# faltou o vinculo ON para ligar a turma com o aluno