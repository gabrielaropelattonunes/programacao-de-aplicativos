ferramentas = ["Chave Inglesa", "Alicate", "Martelo", "Parafusadeira"]

busca = input("Digite o nome da ferramenta que você procura: ")

encontrado = False

for i in range(len(ferramentas)):
    if ferramentas[i].lower() == busca.lower():
        print(f"Peça encontrada na posição {i}!")
        encontrado = True
        break

if not encontrado:
    print("Peça não encontrada.")
    
    while True:
        resposta = input("Deseja adicionar essa peça à lista? (s/n): ").lower()
        
        if resposta == "s":
            ferramentas.append(busca)
            print("Peça adicionada com sucesso!")
            break
        elif resposta == "n":
            print("Peça não adicionada.")
            break
        else:
            print("Resposta inválida. Digite 's' ou 'n'.")

print("Lista final:", ferramentas)