valor = float(input("digite o valor da sua compra "))
cliente = input("digite se for cliente prime S/N ")
frete = 50.0

if valor >= 500.00 or (cliente == "S" and valor >= 100.00):
    print("parabens voce ganhou frete gratis!")
    frente = 0.0
    print("valor_total", valor)

valor_total = valor + frete
print("valor total" , valor_total)