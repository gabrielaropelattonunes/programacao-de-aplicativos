senha = input("digite a sua senha ")
tentativas = int(input("quantas foram suas tentativas "))
token = input("voce possui TOKEN? (S/N) ")

if senha == "admin123" and (tentativas % 3 == 0 or token == "S"):
    print(f"Tentativa nº {tentativas}: ACESSO CONCEDIDO.")
else:
    print(f"Tentativa nº {tentativas}: ACESSO BLOQUEADO POR PROTOCOLO.")
