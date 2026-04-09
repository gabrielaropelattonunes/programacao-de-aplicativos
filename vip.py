lista_vip = []

while True:
    nome = input("Digite o nome do convidado (ou 'fim' para encerrar): ")
    
    if nome.lower() == "fim":
        break
    
    if nome.startswith("A") or nome.startswith("a"):
        lista_vip.append(nome)
    else:
        print("Apenas nomes com A são permitidos no VIP")

print("Lista VIP:", lista_vip)