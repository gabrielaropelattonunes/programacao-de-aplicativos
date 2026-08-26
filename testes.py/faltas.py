def situacao_faltas(faltas):
    if faltas >= 0 and faltas <= 4:
        return "regular"
    elif faltas >= 5 and faltas <= 10:
        return "atenção"
    else:   
        return "reprovado"
 	
assert situacao_faltas(0) == "regular"
assert situacao_faltas(4) == "regular"
assert situacao_faltas(5) == "atenção"
assert situacao_faltas(10) == "atenção"
assert situacao_faltas(11) == "reprovado"
