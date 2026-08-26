def buscar_nome(lista, nome):
 	return nome in lista

def tem_senha_valida(senha):
 	return len(senha) >= 8

assert buscar_nome(["ana","carlos"],"ana") == True
assert buscar_nome(["pedro"],"pedro") == True
assert buscar_nome([],"luis") == False

assert tem_senha_valida("ropelatto") == True
assert tem_senha_valida("nunes") == False
assert tem_senha_valida("") == False

# quando a lista é vazia retorna nada.