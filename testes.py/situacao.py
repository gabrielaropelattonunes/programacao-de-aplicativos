def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    else:
 	    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"

# 5.9 e 6 são casos de limite por que o 6 é o minimo pra ser aprovado e o 5.9 esta logo abaixo do limite e serve pra verificar a mudança de comportamento

assert situacao_aluno (-5) == "Reprovado"