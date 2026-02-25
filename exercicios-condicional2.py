poder_de_ataque = int(input("digite o valor desejado"))
pontos_de_defesa = int(input("digite o valor desejado"))

dano = poder_de_ataque - pontos_de_defesa

if dano <= 0:
    print("o vilao bloqueou o ataque. Danos= 0")
elif dano > 0:
    print("ataque critico! voce calsou dano ao de" , dano)