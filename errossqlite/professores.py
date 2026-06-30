import sqlite3 

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()

# dava erro por que faltava uma virgula dentro do select pois ele só executa se tiver duas variaveis e para "burlar" tem que ter a virgula ali