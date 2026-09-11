import banco
import escola
import estrutura_obrigatoria as turma
import aluno
import sqlite3


banco.inicializar_banco()

def exibir_menu():
    print("1. Cadastrar Escola      2. Listar Escolas      3. Alterar Escola      4. Excluir Escola")
    print("5. Cadastrar Turma       6. Listar Turmas       7. Alterar Turma       8. Excluir Turma")
    print("9. Cadastrar Aluno      10. Listar Alunos      11. Alterar Aluno      12. Excluir Aluno")
    print("0. Sair do Sistema")

while True:
    exibir_menu()
    opcao = input("Selecione uma opção: ")
    
    if opcao == "0":
        print("\nEncerrando o sistema. Até mais!")
        break
        
    try:
    
        if opcao == "1":
            nome = input("Nome da Escola: ")
            cidade = input("Cidade: ")
            escola.cadastrar_escola(nome, cidade)
            print("Escola cadastrada com sucesso!")
            
        elif opcao == "2":
            escolas = escola.listar_escolas()
            for esc in escolas:
                print(f"ID: {escola[0]} | Nome: {escola[1]} | Cidade: {escola[2]}")
                
        elif opcao == "3":
            id_escola = int(input("ID da Escola que deseja alterar: "))
            nome = input("Novo Nome da Escola: ")
            cidade = input("Nova Cidade: ")
            if escola.alterar_escola(id_escola, nome, cidade):
                print(" Escola alterada com sucesso!")
            else:
                print(" Escola não encontrada.")
                
        elif opcao == "4":
            id_escola = int(input("ID da Escola que deseja excluir: "))
            if escola.excluir_escola(id_escola):
                print(" Escola removida com sucesso!")
            else:
                print(" Escola não encontrada.")

        
        elif opcao == "5":
            nome_turma = input("Nome da Turma: ")
            id_escola = int(input("ID da Escola Vinculada: "))
            turma.cadastrar_turma(nome_turma, id_escola)
            print(" Turma vinculada e cadastrada com sucesso!")
            
        elif opcao == "6":
            turmas = turma.listar_turmas()
            for turma in turmas:
                print(f"ID: {turma[0]} | Turma: {turma[1]} | ID Escola Pai: {turma[2]}")
                
        elif opcao == "7":
            id_turma = int(input("ID da Turma que deseja alterar: "))
            nome_turma = input("Novo Nome da Turma: ")
            id_escola = int(input("Novo ID da Escola Vinculada: "))
            if turma.alterar_turma(id_turma, nome_turma, id_escola):
                print(" Turma alterada com sucesso!")
            else:
                print(" Turma não encontrada.")
                
        elif opcao == "8":
            id_turma = int(input("ID da Turma que deseja excluir: "))
            if turma.excluir_turma(id_turma):
                print(" Turma removida com sucesso!")
            else:
                print(" Turma não encontrada.")

        
        elif opcao == "9":
            nome_aluno = input("Nome do Aluno: ")
            idade = int(input("Idade do Aluno: "))
            id_turma = int(input("ID da Turma Vinculada: "))
            aluno.cadastrar_aluno(nome_aluno, idade, id_turma)
            print(" Aluno matriculado e cadastrada com sucesso!")
            
        elif opcao == "10":
            alunos = aluno.listar_alunos()
            for aluno in alunos:
                print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} anos | ID Turma: {aluno[3]}")
                
        elif opcao == "11":
            id_aluno = int(input("ID do Aluno que deseja alterar: "))
            nome_aluno = input("Novo Nome do Aluno: ")
            idade = int(input("Nova Idade: "))
            id_turma = int(input("Novo ID da Turma Vinculada: "))
            if aluno.alterar_aluno(id_aluno, nome_aluno, idade, id_turma):
                print(" Ficha do aluno alterada com sucesso!")
            else:
                print(" Aluno não encontrado.")
                
        elif opcao == "12":
            id_aluno = int(input("ID do Aluno que deseja excluir: "))
            if aluno.excluir_aluno(id_aluno):
                print(" Aluno removido do sistema.")
            else:
                print(" Aluno não encontrado.")
                
        else:
            print("Opção Inválida! Digite um número correspondente do menu.")

    except ValueError:
        print(f"ERRO DE DIGITAÇÃO: Você inseriu letras em um campo que exigia apenas números (como ID ou Idade). Tente novamente.")
        
    except AssertionError as erro_validacao:
        print(f"VALIDAÇÃO NEGADA: {erro_validacao}")
        
    except sqlite3.IntegrityError:
        print(f"ERRO DE INTEGRIDADE RELACIONAL: O ID da tabela pai informado não existe no banco de dados. Cadastre a entidade pai primeiro.")
        
    except sqlite3.Error as erro_banco:
        print(f"ERRO CRÍTICO NO BANCO DE DADOS: {erro_banco}")