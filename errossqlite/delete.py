import sqlite3 

def deletar_escola_antiga():
    id_escola = int(input("id da escola a remover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(f"DELETE FROM escolas WHERE id? = {id_escola}")

    conexao.commit()
    conexao.close()

# faltava um ponto de interrogaçao que mostra o que é pra apagar
# um f e a chave que chama a função id_escola