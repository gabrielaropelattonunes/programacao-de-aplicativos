quantidade = int(input("Quantas garrafas ja passaram pela esteira hoje? "))

if quantidade == 500:
    print("HORA DA LIMPEZA, pare a maquina!")
    print("QUALIDADE, retire a amostra para teste")

elif quantidade % 500 == 0:
    print("HORA DA LIMPEZA, pare a maquina!")

elif quantidade % 100 == 0:
    print("QUALIDADE, retire a amostra para teste")

else:
    print(f"producao em dia. Garrafa numero {quantidade} processada")