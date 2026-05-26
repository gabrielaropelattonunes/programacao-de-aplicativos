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
    print("\n--- Atualizar Aluno ---") # print mostra a mensagem com para atualizar o aluno e o \n quebra a linha na parte do terminal para o texto ficar organizado
    if not os.path.exists(BANCO_DADOS): #o comando if not os.path.exists verifica se o arquivo existe ou nao dentro dentro da variavel banco_dados
        print("Nenhum aluno cadastrado no sistema.") # print mostra a mensagem 
        return  # o return encerra a funçao por que aqui esta sozinho 


    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #open abre o arquivo para a leitura, acha o nome da funçao banco_dados, encoding='utf-8' permite que as palavras tenham acentos, as cria uma variavel que vai ser o arquivo (f) e o with serve pra fechar o arquivo imediatemente depois da leitura
        alunos = json.load(f) # ele armazena os dados do arquivo 'alunos.json' em uma variavel que é alunos
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) #cria uma nova variavel que vai buscar o novo cpf, onde pede para o usuario digite e transforma o numero em inteiro e o input pega o que esta sendo digitado 
    
    for aluno in alunos: # ele percorre cada aluno dentro da lista
        if aluno['cpf'] == cpf_busca: #verifica se o CPF de um aluno específico no sistema é igual ao CPF que você está procurando
            print(f"Editando dados de: {aluno['nome']}") #mensagem para editar os dados do cadastro
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # coloca as informaçoes que ja tem e cria um input e int com as novas coisas que vao ser adicionadas 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']  # coloca as informaçoes que ja tem e cria um input e int com as novas coisas que vao ser adicionadas 
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']  # coloca as informaçoes que ja tem e cria um input e int com as novas coisas que vao ser adicionadas 
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])  # coloca as informaçoes que ja tem e cria um input e int com as novas coisas que vao ser adicionadas 
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']  # coloca as informaçoes que ja tem e cria um input e int com as novas coisas que vao ser adicionadas 
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #open abre o arquivo para a escrever, acha o nome da funçao banco_dados, encoding='utf-8' permite que as palavras tenham acentos, as cria uma variavel que vai ser o arquivo (f) e o with serve pra fechar o arquivo imediatemente depois da leitura
                json.dump(alunos, f, indent=4, ensure_ascii=False) #json.dump guarda a lista alunos e salve no arquivo f no formato do JSON, mais organizado e com os acentos corretos.
            print("Dados atualizados com sucesso!") #mostra a mensagem no terminal 
            return #encerra a funçao pois esta sozinho
            
    print("Aluno não encontrado.") #mensagem no terminal se o nome nao estiver cadastrado


def excluir(): # o def cria a funçao, e o nome da funçao(excluir) onde a funçao vai executar comandos 
    print("\n--- Excluir Aluno ---")  # print mostra a mensagem para excluir alunos e o \n quebra a linha na parte do terminal para o texto ficar organizado
    if not os.path.exists(BANCO_DADOS): # o if cria a funcao, os.path.exists() verifica se o arquivo existe no computador ("alunos.json") que esta armazenado na funcao (banco_dados)
        print("Nenhum aluno cadastrado no sistema.") # mostra a mensagem de nenhum aluno no terminal 
        return # encerra a funcao por que esta sozinho 

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #open abre o arquivo para a leitura, acha o nome da funçao banco_dados, encoding='utf-8' permite que as palavras tenham acentos, as cria uma variavel que vai ser o arquivo (f) e o with serve pra fechar o arquivo imediatemente depois da leitura
        alunos = json.load(f) # ele armazena os dados do arquivo 'alunos.json' em uma variavel que é alunos
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: ")) # pede o id do aluno, o aluno digita,o int transforma em inteiro e o input pega o que esta sendo digitado 
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] # cria uma nova lista onde vai adicionar um novo id e o outro vai ser excluido 
    
    if len(nova_lista) < len(alunos): #o if cria uma nova funçao e dentro dela tem o len e ele conta quantas pessoas tem dentro da nova lista e e verifica se e menor que a lista de alunos
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #open abre o arquivo para a escrever, acha o nome da funçao banco_dados, encoding='utf-8' permite que as palavras tenham acentos, as cria uma variavel que vai ser o arquivo (f) e o with serve pra fechar o arquivo imediatemente depois da leitura
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)  #json.dump guarda a nova lista e salve no arquivo f no formato do JSON, mais organizado e com os acentos corretos.
        print("Aluno removido com sucesso!") # mensagem que aparece no terminal que o aluno foi encontrado e removido 
    else: # se a opcao não existe vai para o else
        print("Aluno não encontrado.") # mensagem que aparece no terminal se o aluno nao foi encontrado

def menu(): # o def cria a funçao, e o nome da funçao(menu) onde a funçao vai executar comandos 
    if not os.path.exists(BANCO_DADOS): # o if cria a funcao, os.path.exists() verifica se o arquivo existe no computador ("alunos.json") que esta armazenado na funcao (banco_dados)
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #open abre o arquivo para a escrever, acha o nome da funçao banco_dados, encoding='utf-8' permite que as palavras tenham acentos, as cria uma variavel que vai ser o arquivo (f) e o with serve pra fechar o arquivo imediatemente depois da leitura
            json.dump([], f) # o json.dump aqui armazena uma lista vazia ([]) no arquivo representado por f.

    while True: # laço de repetiçao que faz ele executar todas as opçoes
        print("\n=== SISTEMA ESCOLAR ===") # mostra a mensagem, quebra a lista e comeca a mostrar as opçoes
        print("1. Cadastrar Aluno") # print com a primeira opçao 
        print("2. Listar Alunos") # print com a segunda opçao 
        print("3. Atualizar Aluno") # print com a terceira opçao 
        print("4. Excluir Aluno") # print com a quarta opçao 
        print("5. Sair") # ultimo print pra sair das opçoes
        
        opcao = input("Escolha uma opção: ") # uma nova variavel, com o input para armazenar ela e para o usuario digitar a opçao que quer 
        
        if opcao == '1': cadastrar() # o if cria uma funcao igual a opçao para o cadastro 
        elif opcao == '2': listar() # o elif cria outra funçao igual a opçao para listar 
        elif opcao == '3': atualizar() # o elif cria outra funçao igual a opçao para atualizar 
        elif opcao == '4': excluir() # o elif cria outra funçao igual a opçao para excluir 
        elif opcao == '5': break # o break serve para quebrar o loop 
        else: print("Opção inválida!") # cria um else ja com a mensagem e com a opçao invalida 

menu() # criada para mostrar o menu no terminal 