media = float(input("digite sua media escolar "))
renda = float(input("digite sua renda familiar "))
escola = input("voce vem de escola publica? S/N ")

if media >= 80.0 and (renda <= 2.000 or escola == "S"):
    print("parabens ganhou bolsa")
else:
    print("nao ganhou bolsa, sentimos muito")