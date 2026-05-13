lista = []
soma = 0 

def somar_carrinho(precos_produtos, somar_valores):
    for item in precos_produtos:
        somar_valores += item 
    if total_compras >=500.00:
        multiplicao = total_compras * 0.10
        subtracao = total_compras - multiplicao
        print (f"Valor do desconto:  {multiplicao}")
        print(f"Valor total da compra: {subtracao}")
    else:
        print(f"Valor original da compra  {total_compras} Reais, não possui desconto. ")    

total_compras = int(input("Digite o valor total da compra: "))

somar_carrinho(lista, soma) 