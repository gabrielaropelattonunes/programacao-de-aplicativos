import sqlite3
def conectar():
    conexao = sqlite3.connect("hospital.db")
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao


def criar_tabelas():
    try:
        conexao = sqlite3.connect('hospital.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        for aluno in cursor.fetchall():
            print(aluno)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS hospitais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crm TEXT NOT NULL,
            id_hospital INTEGER NOT NULL,
            FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
        )
        """)

        conexao.commit()
        conexao.close()

    except sqlite3.Error as erro:
        print("Erro ao criar as tabelas:", erro)

def cadastrar_hospitais():
    try:

        conexao = sqlite3.connect('hospital.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        for aluno in cursor.fetchall():
            print(aluno)

        nome_hospitais = input("digite o nome do hospital: ")
        cidade_hospitais = input("digite a cidade do hospital: ")

        comando_inserir = (f'''
                           INSERT INTO hospitais 
                           (nome_hospitais,cidade_hospitais")
                           VALUES ('{nome_hospitais}','{cidade_hospitais}')
                           ''')
        cursor.execute(comando_inserir)
        conexao.commit()

        cursor.execute("SELECT * FROM hospitais")
        for hospitais in cursor.fetchall():
            print(hospitais)

    except ValueError:
        print("valor invalido")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except TypeError:
        print("erro no tipo dos dados")
    except NameError:
        print("nome invalido")
    finally:
        print("finalizado")

    conexao.close()

def cadastrar_medicos():
    try:
        conexao = sqlite3.connect('hospital.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        for aluno in cursor.fetchall():
            print(aluno)

        nome_medicos = input("digite o nome do medico: ")
        cidade_medicos = input("digite a cidade do medico: ")

        comando_inserir = (f'''
                           INSERT INTO hospitais 
                           (nome_medicos,cidade_medicos")
                           VALUES ('{nome_medicos}','{cidade_medicos}')
                           ''')
        cursor.execute(comando_inserir)
        conexao.commit()

        cursor.execute("SELECT * FROM hospitais")
        for medicos in cursor.fetchall():
            print(medicos)

    except ValueError:
        print("valor invalido")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except TypeError:
        print("erro no tipo dos dados")
    except NameError:
        print("nome invalido")
    finally:
        print("finalizado")

    conexao.close()

def listar_hospitais():
    try:
        conexao = sqlite3.connect('hospital.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM hospitais")
        for hospitais in cursor.fetchall():
            print(hospitais)

    except ValueError:
        print("valor invalido")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except TypeError:
        print("erro no tipo dos dados")
    except NameError:
        print("nome invalido")
    finally:
        print("finalizado")

    conexao.close()

def listar_medicos():
    try:
        conexao = sqlite3.connect('hospital.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM medicos")
        for medicos in cursor.fetchall():
            print(medicos)

    except ValueError:
        print("valor invalido")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except TypeError:
        print("erro no tipo dos dados")
    except NameError:
        print("nome invalido")
    finally:
        print("finalizado")

    conexao.close()