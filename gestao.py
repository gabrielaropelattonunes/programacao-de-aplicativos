ID = int(input("qual seu ID "))
temperatura = float(input("qual a temperatura "))
tempo = int(input("qual o tempo de uso "))

if (ID % 3 == 0 ) and (temperatura > 40 or tempo > 8):
    print(f"funcionario {ID} voce foi escalado para a manutencao preventiva hoje")
else:
    print(f"funcionario {ID} sua máquina opera dentro dos padrões normais")