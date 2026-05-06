def calcular_area (largura,comprimento):
    multiplicar = largura * comprimento 
    return multiplicar
tentativas = 0 
while tentativas < 3:
    print(f"terreno {tentativas + 1}")
    largura = float(input("digite a largura do seu terreno: "))
    comprimento = float(input("digite o comprimento do seu terreno: "))

    area = calcular_area(largura,comprimento)
    print(f"digite a area do seu terreno: {area}")
    tentativas +=1


