def esta_na_lista (lista_nome,busca):
    for nome in lista_nome:
        if nome == busca:
            return "encontrado"
    return "não encontrado"

frutas = ["maça","banana","laranja","manga"]
buscas = input("digite o nome das frutas para buscar: ")
final = esta_na_lista(frutas,buscas)
print(final)