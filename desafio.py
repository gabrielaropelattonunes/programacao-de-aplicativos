nome_do_cliente = input("digite seu nome ")
valor_total = float(input("digite o valor da sua compra "))
distancia_da_entrega = int(input("digite a distancia da entrega "))
cupom_de_desconto = input("digite o cupom ")
frente = 40.0

if valor_total >= 1.000 and cupom_de_desconto == "S":
    desconto = valor_total * 0.20
    total = valor_total - desconto
    print("parabens voce ganhou um mousepad gamer de brinde !")
elif valor_total > 500 and valor_total < 1.000 and cupom_de_desconto == "S":
    desconto = valor_total - desconto * 0.10
    total = valor_total - desconto

if distancia_da_entrega <= 50 and valor_total > 200.00:
    frete = 0.00
    valor_final = valor_total + frete 

elif distancia_da_entrega <= 50 and valor_total > 200:
    frete = 0.00


print ("nome do cliente" , nome_do_cliente)
print("valor total da compra" , valor_total)
print("valor do desconto" , cupom_de_desconto)
print("valor final a pagar" , valor_total)
