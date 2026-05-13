vendas = []

def analisar_vendas(nome, lista_vendas, meta_mensal):
    media_vendas = 0
    for item in lista_vendas:
        media_vendas += item
    media_vendas /= len(lista_vendas)
    if media_vendas >= meta_mensal:
        print(f"O Vendedor {nome} com media {media_vendas}, Bateu a meta!")
    else:
        print(f"O Vendedor {nome} com media {media_vendas}, Não bateu a meta!")
nome_vendedor = input("Digite o nome do vendedor: ")
meta_mes = float(input("Meta do mês: "))           
mais_valores = "Sim"
while mais_valores == "Sim":
    vendas_mês = float(input("Qual o valor das vendas do mês ?: "))
    vendas.append(vendas_mês)
    mais_valores = input("Tem mais valores ? : ")
analisar_vendas(nome_vendedor, vendas, meta_mes)