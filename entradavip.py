idade = int(input("digite sua idade "))
ingresso = input("possui ingresso? S/N ")
lista = input("esta na lista de convidados? S/N")

if (idade >= 18 and ingresso == "S") or lista == "S":
    print("liberado, bem vindo")
else:
    print("acesso negado")

