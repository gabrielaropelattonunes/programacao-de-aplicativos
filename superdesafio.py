livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
escolha = input("digite o livro que quer: ")

if escolha in livros_disponiveis:
    livros_disponiveis.remove(escolha)
    livros_emprestados.append(escolha)
    print(f"emprestimo realizado com sucesso!")
else:
    print("desculpa esse livro não esta no acervo")

devolucao = input("qual livro esta devolvendo? ") 

if devolucao in livros_emprestados:
    livros_emprestados.remove(escolha)
    livros_disponiveis.append(escolha)
    print(f"devolução feita")
else:
    print("o livro não se encontra como emprestado")

del livros_disponiveis[0:2]
print(f"lista de livros disponiveis{livros_disponiveis}")
print(f"lista de livros emprestados{livros_emprestados}")