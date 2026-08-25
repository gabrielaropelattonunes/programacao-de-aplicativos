def calcular_desconto(preco, percentual):
 	return preco - (preco * percentual/100) 
# o erro é que o preço estava diminuindo o percentual 

assert calcular_desconto(100,10) == 90
assert calcular_desconto(200,20) == 160
assert calcular_desconto(50,10) == 45