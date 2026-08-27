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
        conexao.close()
    
    
def cadastrar_rede (nome_rede,site):
    try:
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute('''INSERT INTO redes_cinema 
                       (nome_rede,site) VALUES (?,?)''', (nome_rede,site)
                       )
        
        conexao.commit()
        return "rede cadastrada"

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
            return "listado com sucesso"

    except SyntaxError:
        print("Erro: falha na digitação")
    except NameError:
        print("Erro: nome da variavel inexistente")
    finally:
        conexao.close()
    
    
def alterar_redes(ID_atual,nova_rede,novo_site):
    try: 
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute(f''' SELECT * FROM redes_cinema WHERE ID={ID_atual}''')
        redes = cursor.fetchone()
        if not redes:
            print("nenhuma rede encontrada")     
        else:
    
            comando = f''' UPDATE redes_cinema SET nome_rede = '{nova_rede}',
                        site = '{novo_site}' WHERE id={ID_atual}'''

            cursor.execute(comando)
            conexao.commit()
            return "novos dados atualizados"
    
    except  ValueError:
        print("O ID deve ser um número.")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except NameError:
        print("nome invalido")
    finally:
        conexao.close()
    

def excluir_redes(id_redes):
    try:
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute(f"SELECT * FROM redes_cinema WHERE id = {id_redes}")

        redes = cursor.fetchone()

        if not redes:
            return "Nenhuma rede encontrada."
        else:
            cursor.execute(
                f"DELETE FROM redes_cinema WHERE id = {id_redes}"
            )
            conexao.commit()
            return "rede excluida com sucesso! "
        
    except ValueError:
        print("O ID deve ser um número.")
    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)
    finally:
        conexao.close()   
    

def cadastrar_filial(nome_flial,id_rede):
    try:
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute(f"SELECT * FROM redes_cinema WHERE id = {id_rede}")
        rede = cursor.fetchone()

        if not rede:
            return "A rede informada não existe."
        else:
            cursor.execute('''INSERT INTO cinemas_filiais
                        (nome_filial,id_rede) VALUES (?,?)''', (nome_flial,id_rede)
                        )
            conexao.commit()
            return "filial cadastrada"

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
            return "Nenhuma filial cadastrada."
        else:
            for filial in filiais:
                print("ID:", filial[0])
                print("Nome da filial:", filial[1])
                print("ID da rede:", filial[2])
                conexao.commit()
            return "listado com sucesso"
    
    except SyntaxError:
        print("Erro: falha na digitação")
    except NameError:
        print("Erro: nome da variavel inexistente")
    finally:
        conexao.close()
    

def alterar_filial(ID_filial,nova_filial,novo_id_rede):
    try: 
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        ID_filial = int(input("Digite o ID da filial: "))

        cursor.execute(f''' SELECT * FROM cinemas_filiais WHERE ID={ID_filial}''')
        filial = cursor.fetchone()
        if not filial:
            return "nenhuma filial encontrada"    
        else:
            nova_filial = input("digite o nome da nova filial: ")
            novo_id_rede = int(input("digite o nome do novo id da rede: "))

            cursor.execute(f"SELECT * FROM redes_cinema WHERE id = {novo_id_rede}")
            rede = cursor.fetchone()

        if not rede:
            return "nenhuma filial encontrada"
        else:
            comando = f''' UPDATE cinemas_filiais 
                    SET nome_filial = '{nova_filial}',
                       id_rede = {novo_id_rede} WHERE id={ID_filial}'''

            cursor.execute(comando)
            conexao.commit()
            return "dados da filial alterados"
    
    except  ValueError:
        print("O ID deve ser um número.")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except NameError:
        print("nome invalido")
    finally:
        conexao.close()
   

def excluir_filial (ID_filial):
    try:
        conexao = sqlite3.connect("redes.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute(f"SELECT * FROM cinemas_filiais WHERE id = {ID_filial}")
        filial = cursor.fetchone()

        if not filial:
            return "Nenhuma filial encontrada."
        else:
            cursor.execute(
                f"DELETE FROM cinemas_filiais WHERE id = {ID_filial}"
            )
            conexao.commit()
            return "filial excluida com sucesso! "
        
    except ValueError:
        print("O ID deve ser um número.")
    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)
    finally:
        conexao.close()

def menu():
    try:
        while True:
            print("1 - Cadastrar rede")
            print("2 - Listar redes")
            print("3 - Alterar rede")
            print("4 - Excluir rede")
            print("5 - Cadastrar filial")
            print("6 - Listar filiais")
            print("7 - Alterar filial")
            print("8 - Excluir filial")
            print("0 - Sair")

            opcao = input("Digite uma opção: ")

            if opcao == "1":
                nome_rede = input("digite o nome da rede de academia: ")
                site = input("digite o nome do site: ")
                cadastrar_rede(nome_rede,site)

            elif opcao == "2":
                listar_redes()

            elif opcao == "3":
                ID_atual = int(input("Digite o ID atual: "))
                nova_rede = input("digite o nome da nova rede: ")
                novo_site = input("digite o nome do novo site: ")
                alterar_redes(ID_atual,nova_rede,novo_site)

            elif opcao == "4":
                id_redes = int(input("Digite o ID da rede: "))
                excluir_redes(id_redes)

            elif opcao == "5":
                nome_flial = input("digite o nome da filial da academia: ")
                id_rede = int(input("digite o id da rede de academia: "))
                cadastrar_filial(nome_flial,id_rede)

            elif opcao == "6":
                listar_filial()

            elif opcao == "7":
                ID_filial = int(input("Digite o ID da filial: "))
                nova_filial = input("digite o nome da nova filial: ")
                novo_id_rede = int(input("digite o nome do novo id da rede: "))
                alterar_filial( ID_filial,nova_filial,novo_id_rede)

            elif opcao == "8":
                ID_filial = int(input("Digite o ID da filial: "))
                excluir_filial()

            elif opcao == "0":
                print("Programa encerrado.")
                break
                   
            else:
                print("Opção inválida.")

    except Exception as erro:
        print("Erro no menu:", erro)

cadastrar_tabelas()
menu()

assert cadastrar_rede("mg","mg.ww") == "rede cadastrada"
assert listar_redes() == "listado com sucesso"
assert alterar_redes(2,"cm","cm.ww") == "novos dados atualizados"
assert excluir_redes(4) == "rede excluida com sucesso! "
assert excluir_redes(1) == "Nenhuma rede encontrada."
assert cadastrar_filial("lm ",2) == "filial cadastrada"
assert cadastrar_filial("gm",1) == "A rede informada não existe."
assert listar_filial() == "listado com sucesso"
assert listar_filial() == "Nenhuma filial cadastrada."
assert alterar_filial(1,"star",4) == "dados da filial alterados"
assert excluir_filial(2) == "filial excluida com sucesso! "
assert excluir_filial (9) == "Nenhuma filial encontrada."