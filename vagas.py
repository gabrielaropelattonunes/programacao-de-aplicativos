vagas = ["livre","ocupado","livre","ocupado"]
indice = int(input("digite um numero de 0 a 3: "))

if indice % 2 == 0 and "livre":
    print(f"vaga{indice} autorizado para estacionar")

else:
    print(f"vaga {indice} indisponivel ou fora das regras")