nome = input("digite seu nome ")
altura = float(input("digite sua altura"))

if altura < 1.50 : 
    print("desculpa voce nao tem altura minima (nome)", nome )
elif altura >= 1.50:
    print("acesso liberado! divirta- se na queda livre", nome)
