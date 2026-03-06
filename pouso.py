print("---- DESAFIO TECNICO----")

codigo = int(input("digite o codigo do drone "))
autorizacao = input("voce possui autorizacao da torre, (S/N) ")

if codigo == 999 or autorizacao == "S":
    print("OK,drone identificado!")
    bateria = int(input("qual o nivel da bateria do drone "))
    clima = input("o clima esta ensolarado ou chuvoso?  ")
    vento = int(input("qual a velocidade do vento "))
    
    if bateria <10:
        print("pouso AUTORIZADO IMEDIATAMENTE, por seguranca")
    elif bateria >= 10:
            if (clima == "ENSOLARADO" and vento < 30 ) or (clima == "CHUVOSO" and vento <10):
                print("POUSO AUTORIZADO!")
            else:
                print("POUSO NEGADO, condicoes do clima perigosas")
else:
    print("ERRO:drone nao indentificado!")


