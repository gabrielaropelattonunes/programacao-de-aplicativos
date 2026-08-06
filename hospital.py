import sqlite3

def cadastrar_tabelas():
    try:

        conexao = sqlite3.connect("hospital.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS hospitais(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cidade TEXT NOT NULL
                        )''')


        cursor.execute('''CREATE TABLE IF NOT EXISTS medicos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        crm INTEGER NOT NULL,
                        id_hospital INTEGER NOT NULL,
                        FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
                        )''')

        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar o banco:", erro)
    finally:
        print("finalizado")


def inserir_tabelas():
    try:
        conexao = sqlite3.connect("hospital.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()


        nome_hospital = input("Digite o nome do hospital: ")
        cidade_hospital = input("Digite a cidade do hospital: ")
        nome_medico = input("Digite o nome do medico: ")
        crm_medico = int(input("Digite o CRM: "))
        id_hospital = int(input("ID do hospital: "))


        comando_inserir = f'''
                            INSERT INTO hospitais (nome, cidade)
                            VALUES ('{nome_hospital}', '{cidade_hospital}')'''

        cursor.execute(comando_inserir)
        conexao.commit()

        cursor.execute(f"SELECT * FROM hospitais WHERE id = {id_hospital}")

        if cursor.fetchone():   

            comando_inserir = f'''
                            INSERT INTO medicos (nome, crm, id_hospital)
                            VALUES ('{nome_medico}', '{crm_medico}', '{id_hospital}')'''

            cursor.execute(comando_inserir)
            conexao.commit()

        else:
            print("Erro! Hospital não encontrado.")

    except sqlite3.Error as erro:
            print("Erro:", erro)

    finally: 
        conexao.close()