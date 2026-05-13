nome_usuario = input("Digite o nome de usuario: ")
peso_usuario = int(input("Digite o seu peso: "))
altura_usuario = float(input("Digite a sua altura: "))
idade_usuario = int(input("Digite sua idade: "))
categoria_usuario = ""


def  gerar_relatorio_saude(nome, peso, altura, idade, categoria):
    imc = peso / (altura ** 2)
    if imc <= 18.5:
       categoria = "Baixo peso"
    elif imc >18.5 and imc < 24.9:
       categoria =  "Peso normal"
    elif imc > 25.0 and imc < 29.9:
        categoria ="Sobrepeso0"
    elif imc >= 29.9:
            categoria ="OBESIDADE"
    print(f"Olá  {nome}, idade: {idade}, seu imc: {categoria}  ")      