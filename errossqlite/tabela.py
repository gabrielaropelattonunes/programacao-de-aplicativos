import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    tabelas_permitidas = ["alunos","professores","turma"]

    if nome_tabela not in tabelas_permitidas:
        print("tabela invalida")
        return

    comando = f"SELECT * FROM {nome_tabela} WHERE id = ?"

    cursor.execute(comando,(id_registro))

    conexao.commit()
    print(cursor.fetchone())

    conexao.close()

# não é aceito o caractere (?) por que ele é usado para valores e não para nomes de tabela.