def pode_votar(idade):
 	return idade >= 16

assert pode_votar(14) == False
assert pode_votar(15.5) == False
assert pode_votar(16) == True