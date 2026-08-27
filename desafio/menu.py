from redes import cadastrar_tabelas, cadastrar_rede, listar_redes, alterar_redes, excluir_redes
from filiais import cadastrar_as_tabelas, cadastrar_filial, listar_filial, alterar_filial, excluir_filial


def menu():
    try:
        while True:
            print("1 - Cadastrar rede")
            print("2 - Listar redes")
            print("3 - Alterar rede")
            print("4 - Excluir rede")
            print("5 - Cadastrar filial")
            print("6 - Listar filiais")
            print("7 - Alterar filial")
            print("8 - Excluir filial")
            print("0 - Sair")

            opcao = input("Digite uma opção: ")

            if opcao == "1":
                cadastrar_rede()

            elif opcao == "2":
                listar_redes()

            elif opcao == "3":
                alterar_redes()

            elif opcao == "4":
                excluir_redes()

            elif opcao == "5":
                cadastrar_filial()

            elif opcao == "6":
                listar_filial()

            elif opcao == "7":
                alterar_filial()

            elif opcao == "8":
                excluir_filial()

            elif opcao == "0":
                print("Programa encerrado.")

            else:
                print("Opção inválida.")

    except Exception as erro:
        print("Erro no menu:", erro)

cadastrar_tabelas()
menu()