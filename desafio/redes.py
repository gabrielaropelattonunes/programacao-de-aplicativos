import sqlite3

def cadastrar_tabelas():
    try:
        conexao = sqlite3.connect("redes.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS redes_cinema (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome_rede TEXT NOT NULL,
                            site TEXT NOT NULL
                            )''')
        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar as tabelas:", erro)
    finally:
        print(conexao.close)

def cadastrar_rede():
    try:
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        nome_rede = input("digite o nome da rede de academia: ")
        site = input("digite o nome do site: ")

        cursor.execute('''INSERT INTO redes_cinema 
                       (nome_rede,site) VALUES (?,?)''', (nome_rede,site)
                       )

        conexao.commit()

    except sqlite3.IntegrityError:
        print("Erro: a rede informada não existe.")
    finally:
        conexao.close()

def listar_redes():
    try:
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("SELECT * FROM redes_cinema")
        redes = cursor.fetchall()

        if len(redes) == 0:
            print("Nenhuma rede cadastrada.")
        else:
            for rede in redes:
                print("ID:", rede[0])
                print("Nome:", rede[1])
                print("Site:", rede[2])
            conexao.commit()

    except SyntaxError:
        print("Erro: falha na digitação")
    except NameError:
        print("Erro: nome da variavel inexistente")
    finally:
        conexao.close()

def alterar_redes():
    try: 
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        ID_atual = int(input("Digite o ID atual: "))
        cursor.execute(f''' SELECT * FROM redes_cinema WHERE ID={ID_atual}''')
        redes = cursor.fetchone()
        if not redes:
            print("nenhuma rede encontrada")     
        else:
            nova_rede = input("digite o nome da nova rede: ")
            novo_site = input("digite o nome do novo site: ")

            comando = f''' UPDATE redes_cinema SET nome_rede = '{nova_rede}',
                        site = '{novo_site}' WHERE id={ID_atual}'''

            cursor.execute(comando)
            conexao.commit()
            print("novos dados atualizados")

    except  ValueError:
        print("O ID deve ser um número.")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except NameError:
        print("nome invalido")
    finally:
        conexao.close()

def excluir_redes():
    try:
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        id_redes = int(input("Digite o ID da rede: "))
        cursor.execute(f"SELECT * FROM redes_cinema WHERE id = {id_redes}")

        redes = cursor.fetchone()

        if not redes:
            print("Nenhuma rede encontrada.")
        else:
            cursor.execute(
                f"DELETE FROM redes_cinema WHERE id = {id_redes}"
            )
            conexao.commit()
            print("rede excluida com sucesso! ")

    except ValueError:
        print("O ID deve ser um número.")
    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)
    finally:
        conexao.close()