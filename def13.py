def  calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
    valor_com_imposto = valor_base + (valor_base * (imposto_percentual / 100))
    preco_final = valor_com_imposto - cupom_desconto
    if preco_final < 0:
        return preco_final
    

valor_base = float(input("Digite o valor base do produto: R$ "))
imposto_percentual = float(input("Digite o imposto (%): "))
cupom_desconto = float(input("Digite o valor do cupom de desconto: R$ "))
    
preco_final = calcular_preco_final(valor_base, imposto_percentual, cupom_desconto)
    
print(f"Preço final: R$ {preco_final}")

preco_final = calcular_preco_final(valor_base, imposto_percentual, cupom_desconto)