import json #aqui importamos do python para o json
import os #olha se o arquivo existe 

BANCO_DADOS = 'alunos.json' #variavel que guarda o nome do arquivo

def cadastrar():# o def cria a funçao, e o nome da funçao(cadastrar) onde a funçao vai executar comandos 
    print("\n--- Novo Cadastro ---") # print mostra a mensagem com o novo cadastro e o \n quebra a linha na parte do terminal para o texto ficar organizado
    
    if os.path.exists(BANCO_DADOS): #o if cria a funçao e os.path.exists() verifica se o arquivo existe no computador ("alunos.json") que esta armazenado na funcao (banco_dados)
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #open abre o arquivo para a leitura, acha o nome da funçao banco_dados, encoding='utf-8' permite que as palavras tenham acentos, as cria uma variavel que vai ser o arquivo (f) e o with serve pra fechar o arquivo imediatemente depois da leitura
            alunos = json.load(f) # ele armazena os dados do arquivo 'alunos.json' em uma variavel que é alunos
    else: # se o arquivo não existe vai para o else
        alunos = []# e no else ele cria uma nova lista que esta vazia
   
    novo_aluno = { # cria um dicionario que armazena os dados que estão sendo pedidos, podem ser chamados de valor e chave
        "nome": input("Nome: "), #mostra o que esta pedindo na tela, o usuario digita o que esta pedindo, e o input pega o que esta sendo digitado  
        "telefone": input("Telefone: "), #mostra o que esta pedindo na tela, o usuario digita o que esta pedindo, e o input pega o que esta sendo digitado  
        "turma": input("Turma: "), #mostra o que esta pedindo na tela, o usuario digita o que esta pedindo, e o input pega o que esta sendo digitado  
        "idade": int(input("Idade: ")), #mostra o que esta pedindo na tela, o usuario digita o que esta pedindo, o int transforma o numero em inteiro , e o input pega o que esta sendo digitado  
        "cpf": input("CPF: ") #mostra o que esta pedindo na tela, o usuario digita o que esta pedindo, e o input pega o que esta sendo digitado  
    } #fecha o dicionario novo_aluno
    
    alunos.append(novo_aluno) #adiciona o dicionario novo_aluno dentro da lista de alunos 

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # o open abre o arquivo para a escrita, chama o nome da funçao banco_dados, encoding='utf-8' permite que as palavras tenham acentos, as cria uma variavel que vai ser o arquivo (f) e o with serve pra fechar o arquivo imediatemente depois da leitura
        json.dump(alunos, f, indent=4, ensure_ascii=False) #json.dump guarda a lista alunos e salve no arquivo f no formato do JSON, mais organizado e com os acentos corretos.
        
    print("Aluno cadastrado com sucesso!") #mostra a mensagem no terminal 

def listar(): # o def cria a funçao, e o nome da funçao(listar) onde a funçao vai executar comandos 
    print("\n--- Lista de Alunos ---")  # print mostra a mensagem com a lista de alunos e o \n quebra a linha na parte do terminal para o texto ficar organizado
    
    if os.path.exists(BANCO_DADOS):#o if cria a funçao e os.path.exists() verifica se o arquivo existe no computador ("alunos.json") que esta armazenado na funcao (banco_dados)
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #open abre o arquivo para a leitura, acha o nome da funçao banco_dados, encoding='utf-8' permite que as palavras tenham acentos, as cria uma variavel que vai ser o arquivo (f) e o with serve pra fechar o arquivo imediatemente depois da leitura
            alunos = json.load(f) # ele armazena os dados do arquivo 'alunos.json' em uma variavel que é alunos
    else: # se o arquivo não existe vai para o else
        alunos = [] # e no else ele cria uma nova lista que esta vazia

    if not alunos: #aqui verifica se a lista de alunos esta vazia ou nao
        print("Nenhum aluno cadastrado.") #mostra a mensagem no terminal 
        return # o return encerra a funçao por que aqui esta sozinho 

    for aluno in alunos: # ele percorre cada aluno dentro da lista
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") #nessa linha ele pega os dados de tudo que foi cadastrado no novo_aluno

def atualizar():  # o def cria a funçao, e o nome da funçao(atualizar) onde a funçao vai executar comandos 
    print("\n--- Atualizar Aluno ---") # print mostra a mensagem com a lista de alunos e o \n quebra a linha na parte do terminal para o texto ficar organizado
    if not os.path.exists(BANCO_DADOS): #o comando if not os.path.exists verifica se o arquivo existe ou nao dentro dentro da variavel banco_dados
        print("Nenhum aluno cadastrado no sistema.") # print mostra a mensagem 
        return  # o return encerra a funçao por que aqui esta sozinho 


    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #open abre o arquivo para a leitura, acha o nome da funçao banco_dados, encoding='utf-8' permite que as palavras tenham acentos, as cria uma variavel que vai ser o arquivo (f) e o with serve pra fechar o arquivo imediatemente depois da leitura
        alunos = json.load(f) # ele armazena os dados do arquivo 'alunos.json' em uma variavel que é alunos
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) #cria uma nova variavel que vai buscar o novo cpf, onde pede para o usuario digite e transforma o numero em inteiro e o input pega o que esta sendo digitado 
    
    for aluno in alunos: # ele percorre cada aluno dentro da lista
        if aluno['cpf'] == cpf_busca: #) verifica se o CPF de um aluno específico no sistema é igual ao CPF que você está procurando
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("Dados atualizados com sucesso!")
            return
            
    print("Aluno não encontrado.")

def excluir():
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    
    nova_lista = [a for a in alunos if a['id'] != id_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()