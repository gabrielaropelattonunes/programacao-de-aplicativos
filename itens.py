cores_secretas = ["azul", "preto", "verde"]

tentativas = 0
acertou = False

while tentativas < 3:
    palpite = input("Adivinhe uma cor: ").lower()
    
    if palpite in cores_secretas:
        print("Parabéns, você acertou!")
        acertou = True
        break
    else:
        print("Errou!")
    
    tentativas += 1

if not acertou:
    print("Suas tentativas acabaram!")
    print("As cores corretas eram:", cores_secretas)