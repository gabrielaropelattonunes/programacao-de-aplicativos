def dobrar(numero):
 	return numero * 2

assert dobrar(3) == 6 #P
assert dobrar(0) == 1 #F
assert dobrar(-2) == -4 #P

# o que falhou foi o (assert dobrar(0) == 1) por que pede pra dobrar, o resultado real foi 0, a expectativa era dobrar e se dobrar 0 dá 0.