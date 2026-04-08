peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc}")

if imc > 25:
    print("Você está com sobrepeso.")
else:
    print("IMC dentro do normal.")
