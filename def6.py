def converter_km_para_ms (velocidade_km):
    converter = velocidade_km / 3.6
    return converter 
velocidade = float(input("digite a sua velocidade: "))

if velocidade > 80:
    velocidade_ms = converter_km_para_ms (velocidade)
    print(f"velocidade em ms: {velocidade}")
    print("reduza a velocidade")
else:
    print("velocidade dentro do limite") 