usuario = input("digite seu nome de usuario ")
senha = int(input("digite sua senha "))

if (usuario == "admin" or "root") and senha == 12345:
    print("acesso liberado")
else:
    print("acesso negado")