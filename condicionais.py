salario = float (input("quanto voce recebe"))

if salario >= 10.000:
    print("rico")
elif salario >= 5.000:
    print("classe media")
elif salario < 5.000:
    print("classe baixa")