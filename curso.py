print("----- PRENSA HIDRAULICA -----")
curso = input("voce concluiu o curso de seguranca (S/N)")

if curso == "S":
    instrutor = input("o instrutor esta presente na sala (S/N)")
    if instrutor == "S":
        print("acesso liberado, operacao iniciada")
    else:
        print("aguarde o instrutor para ligar a maquina")

else:
    print("faça o treinamento primeiro")