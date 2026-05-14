def criar_arquivo():
    open("habitos.txt ",'w').close()
criar_arquivo

def adicionar():
    habitos = input("digite os habitos que deseja atualizar: ")
    with open("habitos.txt",'a') as h:
        h.write(habitos + '\n')
        print("novo habito adicionado")

def ler():
    with open("habitos.txt",'r') as h:
        habitos = h.readlines()
    soma = 0 
    for habito in habitos:
        print(f"{soma} - {habito.strip()}")
    soma +=1

def atualizar():
    ler()
    habitos = int(input("digite o id do habito que deseja atualizar: "))
    novos_habitos = input("digite o novo habito: ")
    with open("habitos.txt",'r') as h:
        linhas = h.readlines()
    linhas[habitos] = novos_habitos + '\n'
    with open("habitos.txt",'w') as h:
        h.readlines(linhas)
    print("novos habitos atualizados")

def deletar():
    ler()
    habitos = int(input("digite o id dos habitos que deseja remover: "))
    with open("habitos.txt",'r') as h:
        linhas = h.readlines()
    del linhas[habitos]
    with open("habitos.txt",'w') as h:
        h.writelines(linhas)
    print("habito removido")  

while True:
    print("1-adicionar")
    print("2-ler")
    print("3-ler")
    print("4-atualizar")
    print("5-sair")
    opcao = input("escolha: ")

    if opcao == '1': adicionar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    else:
        print("saindo do programa")