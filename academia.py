import sqlite3

def criar_tabela ():
    try:
        conexao = sqlite3.connect("academia.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute('''CREATE TABLE IF NOT EXISTS academia
                       (id_academia INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT UNIQUE,
                       bairro TEXT)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS alunos
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT,
                       mensalidade TEXT,
                       id_academia INTEGER,
                       FOREIGN KEY (id_academia) REFERENCES academia (id_academia))''')
        conexao.commit()
    finally:
        conexao.close()
        
        




def cadastar_academia(nome, bairro):
    try:
        conexao = sqlite3.connect("academia.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''INSERT INTO academia
                       (nome, bairro) values (?, ? )''',(nome, bairro) )
        print("Academia cadastrada com sucesso!")
        conexao.commit()
    finally:
        conexao.close()

def cadastrar_aluno(nome, mensalidade, id_academia):
    try:
        conexao = sqlite3.connect("academia.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''INSERT INTO alunos 
                    (nome, mensalidade, id_academia) VALUES (?, ?, ?) ''', (nome, mensalidade, id_academia))
        conexao.commit()
        print(f"Aluno {nome} cadastrado com sucesso! ")
    except sqlite3.IntegrityError:
        print("Aluno inexistente")
    finally:
        conexao.close()


def ler():
    conexao = sqlite3.connect("academia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("SELECT * FROM alunos")
    alunos_cadastrados = cursor.fetchall()
    for aluno in alunos_cadastrados:
        print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Mensalidade: R${aluno[2]:.2f} | ID Academia: {aluno[3]}")
    conexao.commit()
    conexao.close()

def menu():
    while True:
        print("1-CADASTRAR ACADEMIA| 2-CADASTRAR ALUNO | 3-VERIFICAR ALUNOS |4- SAIR")
        opcao = input("Digite a opção: ")
        if opcao == "1" :
            nome = input("Digite o nome da unidade: ")
            bairro = input("Digite o bairro da unidade: ")
            cadastar_academia(nome, bairro)

        elif opcao == "2":
            id_acad = int(input("Digite o ID da academia: "))
            nome_aluno = input("Digite o nome do aluno: ") 
            mensalidade = input("Digite o valor da mensalidade: ")
            cadastrar_aluno(nome_aluno, mensalidade,  id_acad) 
        elif opcao == "3":
            ler()
        elif opcao == "4":
            print("Saindo do sistema....")
            break
   

criar_tabela()
menu()