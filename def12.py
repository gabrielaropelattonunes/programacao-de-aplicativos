def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    if possui_certificacao or (nota_teste > 80 and anos_xp > 2):
        return True
    else:
        return False

nota = float(input("Digite a nota do teste: "))
experiencia = int(input("Digite os anos de experiência: "))
certificacao = input("Possui certificação? : ")  

possui_certificacao = certificacao == "sim"

if verificar_aprovacao(nota, experiencia, possui_certificacao):
    print("Resultado: Contratar")
else:
    print("Resultado: Reprovado")  