vida_atual = 1000
def sofrer_dano (vida_atual,valor_dano):

    while vida_atual > 0:
        if valor_dano > vida_atual:
            return "dano critico, game over"
        vida_atual -= valor_dano
        print(vida_atual)
        valor_dano = int(input("qual foi o valor do seu dano?: "))
    return "game over"

valor_dano = int(input("digite seu dano: "))
total = sofrer_dano(vida_atual,valor_dano)
print(total)



