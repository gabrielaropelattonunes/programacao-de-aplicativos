def senha_valida (senha):
    while len(senha) <6:
        print("senha invalida")
        senha = input("digite a senha novamente: ")
    
    if len(senha) >= 6:
        return "senha cadastrada com sucesso"
    
senha_usuario =input("digite sua senha: ")
senhas= senha_valida(senha_usuario)
print(senhas)