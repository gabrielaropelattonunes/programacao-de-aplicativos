import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    dados = cursor.fetchall()

    print("primeiro print:", dados)
    print("segundo print: ",dados)

    conexao.close()

# o erro era no fetchall por que não tinha uma variavel para armazenar então ia executar tudo de uma vez e no outro print ia ficar vazio
# criamos para armazenar ele e assim ele vai executar tudo certo