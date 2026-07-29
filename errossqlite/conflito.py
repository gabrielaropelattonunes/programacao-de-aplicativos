import sqlite3 
 
def cadastrar_escola_manual():
    conexao = none

	try:
        id_escola = int(input("Digite o ID para a nova escola: ")) 
        nome = input("Nome da escola: ") 
        
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
        
        
        cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola, nome)) 
        
        conexao.commit() 
        print("escola cadastrada!")

    except sqlite3.IntegrityError:
        print("Erro: já existe uma escola com esse ID.")
    
    except sqlite3.Error as e:
        print("erro no banco de dados {e}")

    finally:
        if conexao:
            conexao.close()

# não existe como tratar o erro de um id duplicado se ocorrer o id o programa vai fechar
