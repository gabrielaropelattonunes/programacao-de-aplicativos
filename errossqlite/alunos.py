import sqlite3

def vincular_aluno_turma():
    nome = input("nome do aluno: ")
    try:
        id_turma = int(input("digite o id numerico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?,?)",(nome,
id_turma))
        conexao.commit()
    except sqlite3.Error:
        print("erro no banco de dados!")
    except ValueError:
        print("valor invalido")
    finally:
        conexao.close()

# erro por que o id é int, então se escrever sem ser em numero vai dar erro
# erro que falta um except para pegar o erro de escrita no id 