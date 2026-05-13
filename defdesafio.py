estoque = []
acao = 0
# funcao que adiciona item na lista
def adicionar_lista (nome,estoque):
    estoque.append(nome)

#Funcao que percorre a lista e mostra itens da lista
def listar_produtos(estoques):
    for nome in estoques:
        indice = estoques.index(nome)
        print(f"Posição: {indice} Nome: {nome}")
    print("Lista vazia!")

# atualiza a lista
def atualizar_produto(indice, novo_nome, estoque ):
    estoque[indice] = novo_nome

#remove o item da lista
def remover_produto (indice):
      remover = estoque.pop(indice)
      print(f"Item {remover} removido !")

#exibir o menu
def exibir_menu(acao):
    while acao != 5:  
        print("--------PROGRAMA INICIADO---------")
        print("1: ADICIONAR LISTA")
        print("2: LISTAR PRODUTOS")
        print("3: ATUALIZAR PRODUTO")
        print("4: REMOVER PRODUTO")
        print("-----5 FECHAR PROGRAMA--------")
        acao = int(input("Digite a opção desejada: "))

        if acao == 1:
            digitar_nome = input("Digite o nome que deseja adicionar: ")
            adicionar_lista(digitar_nome, estoque)
        elif acao == 2:
            listar_produtos(estoque)
        elif acao == 3:
            atualizar = input("Digite o nome do produto que deseja atualizar: ")
            indice = estoque.index(atualizar)
            novo_nome = input("Digite o novo nome: ")
            atualizar_produto(indice,novo_nome,estoque)
        elif acao == 4:
            remover = input("Digite o produto que deseja remover: ")
            indice = estoque.index(remover)
            remover_produto(indice)
        elif acao == 5 :
            return 
    
exibir_menu(acao)                    