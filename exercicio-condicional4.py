temperatura = float(input("digite a temperatura"))

if temperatura >= 80:
   print("PERIGO! desligando servidor por superaquecimento")
elif temperatura >= 50 < 80:
    print("alerta: ventoinhas ligadas no máximo!")
elif temperatura < 50:
    print("temperatura estável. Sistema operando normalmente ")
