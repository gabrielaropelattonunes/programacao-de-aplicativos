import sqlite3

def cadastrar_aluno():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor ()
    nome_aluno= input("Digite o nome do aluno: ")
    telefone_aluno= input("Digite o telefone do aluno: ")
    turma_aluno= input("Digite a turma do aluno: ")
    idade_aluno = int(input("Digite a idade do aluno: "))
    cpf_aluno =input("Digite o CPF do aluno: ")

    cursor.execute ('''
                CREATE TABLE IF NOT EXISTS alunos
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    turma TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE
                )''')


    comando_inserir = (f'''
                        insert into alunos
                        (nome, telefone, turma, idade, cpf)
                        values('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}',
                        {idade_aluno}, '{cpf_aluno}')
                        ''')
    
    cursor.execute(comando_inserir)
    conexao.commit()

    cursor.execute("SELECT * FROM alunos")
    for aluno in cursor.fetchall():
        print(aluno)
    conexao.close()

def listar_aluno():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    for aluno in cursor.fetchall():
        print(aluno)
    conexao.close()        


def alterar_aluno():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    ID_atual = int(input("Digite o ID atual: "))
    cursor.execute(f''' SELECT * FROM alunos WHERE ID={ID_atual}''')
    aluno= cursor.fetchone()
    if not aluno:
        print("aluno não encontrado")     
    else:
        novo_nome=input("Digite o novo nome: ")
        nova_idade = input("Digite a nova idade: ")
        novo_telefone = input("Digite o novo telefone: ")
        nova_turma = input("Digite a nova turma: ")
        novo_cpf = input("Digite o novo cpf: ")

    comando= f''' UPDATE alunos SET nome= '{novo_nome}',
                idade= {nova_idade}, telefone= '{novo_telefone}', idade='{nova_idade}',
                turma = '{nova_turma}', cpf= '{novo_cpf}' WHERE id={ID_atual}'''

    cursor.execute(comando)
    conexao.commit()
    print("novos dados atualizados")
    conexao.close()


def excluir_aluno():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_aluno = int(input("Digite o ID do aluno: "))
    cursor.execute(f''' DELETE FROM  alunos 
                    WHERE id = {id_aluno}''') 
    print("aluno excluido com sucesso! ")
    conexao.commit()
    conexao.close()  


while True:
    print("1-CADASTRAR | 2- LISTAR | 3- ALTERAR | 4- EXCLUIR | 5- SAIR ")
    opcao = input("Digite a opção: ")
    if opcao == "1" : cadastrar_aluno()
    elif opcao =="2": listar_aluno()
    elif opcao =="3": alterar_aluno()
    elif opcao== "4": excluir_aluno()
    elif opcao == "5": break