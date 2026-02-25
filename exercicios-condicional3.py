valor_da_compra = float(input("digite o valor total da compra"))
cupom = input("digite o cupom ")

if cupom == "DEV10":
    desconto = valor_da_compra * 0.10
    total = valor_da_compra - desconto
    print("novo valor ", total)
else:
    print("cupom invalido. valor original: R$" , valor_da_compra)
    