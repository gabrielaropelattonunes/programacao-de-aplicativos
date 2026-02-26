media = float(input("digite sua media "))
presenca = int(input("digite sua porcentagem "))

if media >= 70 and presenca >= 75:
    print("parabens! voce foi aprovado")
elif media < 70 and presenca < 75:
    print("reprovado, verifique sua nota ou presenca")