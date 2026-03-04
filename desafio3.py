saldo = 1000.00
menu = input("escolha 1 para deposito, 2 para saque e 3 para extrato ")
print("1- deposito")
print("2- saque")
print("3- extrato")


if menu == "1":
    valor = float(input("digite o seu valor: "))
    if valor > 0.00:
        total = valor + saldo 
        print("o valor depositado foi " , total)

elif menu == "2":
    valor = float(input("digite o seu valor desejado: "))
    if valor > 0 and (valor <= saldo or valor == 100):
        print("o valor sacado foi " , valor)

elif menu == "3":
    print("seu saldo atual e" , saldo)