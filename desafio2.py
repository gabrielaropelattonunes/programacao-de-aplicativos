cargo = input("digite seu cargo ")
codigo = int(input("dgite seu codigo "))
botao = input("o botao de emergencia esta ligado?(S/N)")
epi = input("voce esta utilizando o epi? (S/N)")

if cargo == "engenheiro" or "tecnico" and (codigo == "1234" or botao == "S"):
    print("acesso liberado!")
else:
    print("acesso negado")