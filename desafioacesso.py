autorizados = ["alice","bob","carlos"]
nome = input("digite um nome de um pesquisador: ")

if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"o acesso permitido! o pesquisador {nome} está na posição {indice}")

    remover = input("voce gostaria de remover esse perquisador da lista (s/n)")
    if remover == "s":
        autorizados.remove(nome)
        print(f"lista atual {autorizados}")
    else:
        print("saindo do programa...")
else:
    print(f"acesso negado! o pesquisador {nome} não foi encontrado")
    cadastrar = input("voce gostaria de cadastrar esse pesquisador? (s/n): ")
    if cadastrar == "s":
        autorizados.append(nome)
        print("o pesquisador foi cadastrado")
        print(f"nova lista {autorizados}")
    else:
        print("nem uma alteração foi feita")