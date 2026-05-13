open("viagens.txt",'w').close 

def adicionar():
    destino = input("Digite o destino: ")
    with open("viagens.txt",'a') as arquivo:
        arquivo.append(destino + '\n')
        print("destino adicionado")

def ler():
    with open("viagens.txt",'r') as arquivo:
        viagens = arquivo.readlines()
    soma = 0 
    for viagem in viagens:
        print("f{i} - {viagem.strip()}")
    soma += 1 

def atualizar():
    ler()
    destino = input("digite o destino que deseja alterar: ")
    novo_destino = input("digite o novo destino: ")
    with open("viagens.txt",'r') as arquivo:
        linhas = arquivo.readlines()
    linhas[destino] = novo_destino + '\n'
    with open("viagens.txt",'w') as arquivo:
        arquivo.writelines(linhas)
    print("destino atualizado")

def deletar():
    ler()
    destino =input("digite o destino que deseja remover: ")
    with open("arquivo.txt",'r') as arquivo:
        linhas = arquivo.readlines()
    del linhas [destino]  
    with open("arquivo.txt",'w') as arquivo:
        arquivo.writelines(linhas)
    print("aluno removido")

while True:
    print("\n1-adicionar | 2-Ler | 3-atualizar | 4-deletar | 5-Sair")
    opcao = input("Escolha: ")

    if opcao == '1': adicionar ()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    else:
        print("saindo do programa")