import sqlite3

def cadastrar_tabelas():
    try:

        conexao = sqlite3.connect("cinema.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS cinemas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_cinema TEXT NOT NULL,
                        shopping_cinema TEXT NOT NULL
                        )''')


        cursor.execute('''CREATE TABLE IF NOT EXISTS salas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        numero_sala TEXT,
                        capacidade TEXT,
                        id_cinema INTEGER NOT NULL,
                        FOREIGN KEY (id_cinema) REFERENCES cinemas(id)
                        )''')

        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar o banco:", erro)
    finally:
        print("finalizado")

def cadastrar_sala(numero_sala, capacidade, id_cinema):
    try:
        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''INSERT INTO salas
                       (numero_sala, capacidade, id_cinema) VALUES (?, ?, ?)''', (numero_sala, capacidade, id_cinema))
        conexao.commit()
        print(f"Sala {numero_sala} cadastrada com sucesso! ")
    except sqlite3.IntegrityError:
        print("Sala inexistente")
    finally:
        conexao.close

def cadastrar_cinema(nome, shopping):
    try:
        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO cinemas (nome, shopping) VALUES (?, ?)", (nome, shopping))
        conexao.commit()
        print("Cinema cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Sala inexistente")
    finally:
        conexao.close()

def listar_cinemas():
    try:
        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()
        print("\nLista dos cinemas:")
        cursor.execute("SELECT id_cinema, nome, shopping FROM cinemas")
        todos = cursor.fetchall()
        if todos:
            for c in todos:
                print(f"ID: {c[0]} | Nome: {c[1]} | Shopping: {c[2]}")
        else:
            print("Nenhum cinema cadastrado.")
    except sqlite3.IntegrityError:
        print("Sala inexistente")
    finally:
        conexao.close()

def listar_sala():
    try:
        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        print("Lista das salas ")
        cursor.execute(''' SELECT id_sala, numero_sala, capacidade, id_cinema FROM salas''')
        todas_salas = cursor.fetchall()
        if todas_salas:
            for sala in todas_salas:
                print(f"ID registro: {sala[0]} | sala N: {sala[1]} | capacidade: {sala[2]} lugares | id cinema {sala[3]}")
    except sqlite3.IntegrityError:
        print("Nenhuma sala cadastrada! ")
    finally:
        conexao.close()

def menu():
    while True:
        print("-----Sistema de cinema-----")
        print("1-CADASTRAR CINEMAS | 2-LISTAR CINEMAS | 3-CADASTRAR SALAS | 4-LISTAR SALAS | 3-SAIR")
        opcao = int(input("Digite a opção: "))
        if opcao == 1 :
            print("----1 CADASTRO CINEMA-----")
            cidade = input("Digite a cidade: ")
            shopping = input("Digite o nome do shopping: ")
            cadastrar_cinema(cidade, shopping)
        elif opcao == 2:
            print("----2 LISTA DE CINEMAS----")
            listar_cinemas()
        elif opcao == 3:
            print("-------3 CADASTRO DE SALA-------")
            numero = int(input("Digite o numero da sala: "))
            capacidade = int(input("Digite a capacidade da sala: "))
            id_cinema = int(input("Digite o ID do cinema: "))
            cadastrar_sala(numero, capacidade, id_cinema)
        elif opcao == 4:
            print("------4 LISTA DE SALAS ")
            listar_sala()

cadastrar_tabelas()
menu()