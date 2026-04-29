def aplicar_promocao (lista_precos, nova_lista):
    for precos in lista_precos:
        if precos >= 100.0:
            desconto = precos * 0.15
            novo_valor = precos - desconto
            nova_lista.append(precos)
    return nova_lista

compras = [150.0, 80.0, 200.0, 50.0]
lista = []
compra_atual = aplicar_promocao(compras,lista)
print(compra_atual)