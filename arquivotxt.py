def criar_arquivo():    
    open("viagens.txt",'w').close() 


def adicionar():
    destino = input("Digite o destino: ")
    with open("viagens.txt",'a') as arquivo:
        arquivo.write(destino + '\n')
        print("destino adicionado")

def ler():
    with open("viagens.txt",'r') as arquivo:
        viagens = arquivo.readlines()
    soma = 0 
    for viagem in viagens:
        print(f"{soma} - {viagem.strip()}")
    soma += 1 

def atualizar():
    ler()
    destino = int(input("digite o id que deseja alterar: "))
    novo_destino = input("digite o novo destino: ")
    with open("viagens.txt",'r') as arquivo:
        linhas = arquivo.readlines()
    linhas[destino] = novo_destino + '\n'
    with open("viagens.txt",'w') as arquivo:
        arquivo.writelines(linhas)
    print("destino atualizado")

def deletar():
    ler()
    destino = int(input("digite o id que deseja remover: "))
    with open("viagens.txt",'r') as arquivo:
        linhas = arquivo.readlines()
    del linhas [destino]  
    with open("viagens.txt",'w') as arquivo:
        arquivo.writelines(linhas)
    print("destino removido")

while True:
    print("\n1-adicionar | 2-Ler | 3-atualizar | 4-deletar | 5-Sair")
    opcao = input("Escolha: ")

    if opcao == '1': adicionar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    else:
        print("saindo do programa")