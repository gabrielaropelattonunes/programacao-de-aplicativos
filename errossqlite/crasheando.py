import sqlite3

def cadastrar_serie_seguro(nome, id_escola):
    conexao = None
    try:
        conexao = sqlite3.connect('/pasta_protegida/sistema.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?,?)",
nome,id_escola)
        conexao.commit()
    except sqlite3.Error as e:
        print("erro tecnico:", e)
    finally:
        if conexao:
            conexao.close()

# tava dando erro por que a conexão pode dar erro e se der erro o finally vai fechar algo que deu erro 
# ai adicionamos a conexao