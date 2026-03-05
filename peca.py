print ("inspetor de qualidade")
comprimento = input("digite o seu comprimento esta entre 10 cm ou 12 cm, responda com (S/N)")

if comprimento == "S":
    
    largura = input("digite se a largura esta entre 5cm e 6 cm, responda com (S/N)")
    if largura == "S":
        print("peca aprovada")
    else:
        print("repovado, peca invalida")
else:
    print("repovado, peca invalida")
   
   