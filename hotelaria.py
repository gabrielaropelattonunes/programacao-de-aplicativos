import sqlite3

def conectar_banco():
  try:
    conexao = sqlite3.connect("hotelaria.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS hoteis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS quartos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER NOT NULL,
                preco_diaria REAL NOT NULL,
                id_hotel INTEGER NOT NULL,
                FOREIGN KEY (id_hotel) REFERENCES hoteis(id)
            )
        """)
    conexao.commit()
    return conexao
  except sqlite3.Error as e:
    print(f"Erro ao inicializar o banco de dados: {e}")

def cadastrar_quarto(numero, preco_diaria, id_hotel):
    conexao = sqlite3.connect("hotelaria.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO quartos (numero, preco_diaria, id_hotel) VALUES (?, ?, ?)",
        (numero, preco_diaria, id_hotel),
    )
    conexao.commit()
    print("Quarto cadastrado com sucesso!")  
    conexao.close()


def menu():
    while True:
        print("\n--- MENU HOTELARIA ---")
        print("1. Cadastrar Quarto")
        print("2. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("------CADASTRO DE QUARTO----")
            numero = int(input("Digite o número do quarto: "))
            preco_diaria = float(input("Digite o preço da diária: "))
            id_hotel = int(input("Digite o ID do hotel associado: "))
            cadastrar_quarto(numero, preco_diaria, id_hotel)
        elif opcao == "2":
            print("Encerrando o programa..... ")
        break

conectar_banco()
menu()