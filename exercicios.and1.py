idade = int(input("digite sua idade "))
saldo = float(input("digite seu saldo "))

if idade >= 18 and saldo >= 50.0:
    print("acesso autorizado! Bem-vindo ao evento")
elif idade < 18 and saldo < 50.0:
    print("infelizmente voce nao cumpre os requisitos de entrada")