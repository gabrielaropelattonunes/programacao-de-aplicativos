import sqlite3 
 
def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
        cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
        conexao.commit() 
    except sqlite3.IntegrityError:
        print("CPF já cadastrado")
    except sqlite3.Error: 
        print("erro de sintaxe") 
    finally: 
        conexao.close() 

# o primeiro erro era que no cursor.execute o INSERT tava escrito errado
# tivemos que criar mais um except por que o sqlite3.Error pega todos os erros que existem no codigo e como tinha outro erro no codigo estava dando erro ai criamos um except especifco para o cpf duplicado