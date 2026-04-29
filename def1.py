def avaliar_desempenho (notas):
    if notas >= 9:
        return "excelente"
    elif notas >= 7:
        return "bom"
    elif notas >= 5:
        return "regular"
    else:
        return "insuficiente"

nota = int(input("digite sua nota: "))
resposta = avaliar_desempenho(nota)
print(resposta)