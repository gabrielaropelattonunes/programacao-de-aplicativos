def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "frio"
    elif temperatura >= 15 and temperatura <= 25:
        return "agradavel"
    else:
        return "quente"

assert classificar_temperatura(14) == "frio"
assert classificar_temperatura(20) == "agradavel"
assert classificar_temperatura(10.5) == "frio"
assert classificar_temperatura(28) == "quente"
assert classificar_temperatura(18.8) == "agradavel"
assert classificar_temperatura(30.6) == "quente"