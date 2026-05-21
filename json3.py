import json 

def criar_arquivo():
    open("alunos.json",'w').close()

def listar_dados(dados):
    with open("alunos.json",'r') as a:
        json.dump(dados,a,indent=4)

def cadastrar_alunos(dados,cpf):
    dados = listar_dados()
    nome = input("digite o nome do aluno: ")
    telefone = int(input("digite o telefone do aluno: "))
    turma = input("digite a turma do aluno: ")
    idade = int(input("digite a idade do aluno: "))
    cpf = int(input("digite o CPF do aluno: "))


    alunos = {
        "nome": nome,
        "telefone": telefone,
        "turma": turma,
        "idade": idade,
        "cpf": cpf
    }

def listar_alunos():
    with open("alunos.json",'r') as a:
        dados = json.load(a)
print()

def atualizar_dados():
    with open("alunos.json",'r') as a:
        dados = json.load(a)
        dados['telefone'] 



def remover_aluno():
    with open("alunos.json",'r') as a:
        dados = json.load(a)
    if 'cpf' in dados:
        del dados ['cpf']
        print("campo 'cpf' removido com sucesso")
    with open("alunos.json",'w',encoding='utf-8') as a:
        json.dump(dados,a,indent=4,ensure_ascii=False)