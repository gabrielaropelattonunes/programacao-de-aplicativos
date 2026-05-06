def contar_caracteres(palavra):
    while len(palavra) < 5:
        print("palavra muito curta")
        palavra = input("digite uma palavra novamente: ")
    print("palavra aceita")

palavra_usuario = input("digite a sua palavra: ")
contar_caracteres(palavra_usuario)