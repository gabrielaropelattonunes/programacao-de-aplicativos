import json

frase = input("digite uma mensagem: ")
dicionario = {"mensagem": frase} 

with open("teste.json","w") as i:
    json.dump(dicionario, i, ensure_ascii=False, indent=4)
    print("Arquivo teste.json criado com sucesso!")