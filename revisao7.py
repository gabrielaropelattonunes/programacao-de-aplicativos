nomes = ["ana", "alice", "joao", "gustavo", "maria", "vitoria"]
verificar = input("digite seu nome de verificaçao: ")

if verificar in nomes:
    print(f"O nome {verificar} está na lista!")
else:
    print(f"O nome {verificar} não foi encontrado na lista.")
