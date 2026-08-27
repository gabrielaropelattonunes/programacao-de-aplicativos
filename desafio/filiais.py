import sqlite3

def cadastrar_as_tabelas():
    try:
        conexao = sqlite3.connect("redes.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS cinemas_filiais (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome_filial TEXT NOT NULL,
                            id_rede INTEGER NOT NULL,
                            FOREIGN KEY (id_rede) REFERENCES redes_cinema(id)
                            )''')

        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar as tabelas:", erro)
    finally:
        print(conexao.close)

def cadastrar_filial():
    try:
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        nome_flial = input("digite o nome da filial da academia: ")
        id_rede = int(input("digite o id da rede de academia: "))

        cursor.execute(f"SELECT * FROM redes_cinema WHERE id = {id_rede}")
        rede = cursor.fetchone()

        if not rede:
            print("A rede informada não existe.")
        else:
            cursor.execute('''INSERT INTO cinemas_filiais
                        (nome_filial,id_rede) VALUES (?,?)''', (nome_flial,id_rede)
                        )
            conexao.commit()
            print("filial cadastrada")
    except  sqlite3.Error as erro:
        print("Erro ao criar as tabelas:", erro)
    except sqlite3.IntegrityError:
        print("Erro: a rede informada não existe.")
    finally:
        conexao.close()

def listar_filial():
    try:
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("SELECT * FROM cinemas_filiais")
        filiais = cursor.fetchall()

        if len(filiais) == 0:
            print("Nenhuma filial cadastrada.")
        else:
            for filial in filiais:
                print("ID:", filial[0])
                print("Nome da filial:", filial[1])
                print("ID da rede:", filial[2])
                conexao.commit()

    except SyntaxError:
        print("Erro: falha na digitação")
    except NameError:
        print("Erro: nome da variavel inexistente")
    finally:
        conexao.close()

def alterar_filial():
    try: 
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        ID_filial = int(input("Digite o ID da filial: "))

        cursor.execute(f''' SELECT * FROM cinemas_filiais WHERE ID={ID_filial}''')
        filial = cursor.fetchone()
        if not filial:
            print("nenhuma filial encontrada")     
        else:
            nova_filial = input("digite o nome da nova filial: ")
            novo_id_rede = int(input("digite o nome do novo id da rede: "))

            cursor.execute(f"SELECT * FROM redes_cinema WHERE id = {novo_id_rede}")
            rede = cursor.fetchone()

        if not rede:
            print("nenhuma filial encontrada")
        else:
            comando = f''' UPDATE cinemas_filiais SET nome_filial = '{nova_filial}',
                       id_rede = {novo_id_rede} WHERE id={ID_filial}'''

            cursor.execute(comando)
            conexao.commit()
            print("dados da filial alterados")

    except  ValueError:
        print("O ID deve ser um número.")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except NameError:
        print("nome invalido")
    finally:
        conexao.close()

def excluir_filial ():
    try:
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        ID_filial = int(input("Digite o ID da filial: "))
        cursor.execute(f"SELECT * FROM cinemas_filiais WHERE id = {ID_filial}")
        filial = cursor.fetchone()

        if not filial:
            print("Nenhuma filial encontrada.")
        else:
            cursor.execute(
                f"DELETE FROM cinemas_filiais WHERE id = {ID_filial}"
            )
            conexao.commit()
            print("filial excluida com sucesso! ")

    except ValueError:
        print("O ID deve ser um número.")
    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)
    finally:
        conexao.close()
