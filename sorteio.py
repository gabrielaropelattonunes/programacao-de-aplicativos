usuario = int(input("digite o seu id do usuario "))
valor = float(input("digite o valor da sua compra "))

if usuario % 2 == 0 and valor > 500.00:
    print(f"parabens usuario {usuario}!voce ganhou um cupom para sua compra de R${valor}")
else:
    print(f"obrigada pela compra, usuario {usuario}. Continue acompanhado as promocoes")
