print("----- ESTUFA INTELIGENTE -----")
temperatura = float(input("qual a temperatura da estufa"))

if temperatura <= 30:
    print("clima estavel")
else:
    print("alerta de calor")

umidade = float(input("qual a umidade "))
if umidade < 40:
    print ("'acao ligar irrigacao!")
else:
    print("acao ligar apenas ventiladores!")