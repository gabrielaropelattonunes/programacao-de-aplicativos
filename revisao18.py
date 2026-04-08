numeros = [12, 45, 7, 89, 23, 56]

maior_valor = numeros[0]

for n in numeros:
    if n > maior_valor:
        maior_valor = n

print(f"O maior valor é: {maior_valor}")