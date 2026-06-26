import sqlite3


def criar_tabela():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        nome = input("Digite o nome completo do professor: ")
        tel = input("Digite o telefone: ")
        materia = input("Digite a materia: ")
        idade = int(input("Digite a idade: "))
        salario = input("Digite o salário: ")
        endereco= input("digite o endereço: ")
        cidade = input("digite a cidade do professor: ")
        estado = input("digite o estado: ")
        nome_escola = input("Digite o nome da escola que trabalha: ")

        cursor.execute ('''
                    CREATE TABLE IF NOT EXISTS professor
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        telefone TEXT,
                        materia TEXT,
                        idade INTEGER,
                        salario TEXT,
                        endereco TEXT,
                        cidade TEXT,
                        estado TEXT,
                        nome_escola  TEXT )''')
        
        comando_inserir = (f'''
                            INSERT INTO professor
                            (nome, telefone, materia, idade, salario, endereco, cidade, estado, nome_escola)
                            VALUES('{nome}', '{tel}', '{materia}',
                            {idade}, '{salario}' ,'{endereco}', '{cidade}', '{estado}','{nome_escola}')''')
        cursor.execute(comando_inserir)
        conexao.commit()
        cursor.execute("SELECT * FROM professor")
        for professor in cursor.fetchall():
            print(professor)

    except ValueError:
        print("valor invalido")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except TypeError:
        print("erro de tipos de dados")
    except NameError:
        print("nome invalido")
    except IndexError:
        print("posição que não existe")
    except KeyError:
        print("chave não encontrada")
    except AttributeError:
        print("atributo não existe")
    except Exception as e:
        print(f"ocorreu um erro {e}")
    finally:
        print("finalizado")

    conexao.close()

def listar():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM professor")
        for aluno in cursor.fetchall():
            print(aluno)

    except ValueError:
        print("valor invalido")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except TypeError:
        print("erro de tipos de dados")
    except NameError:
        print("nome invalido")
    except IndexError:
        print("posição que não existe")
    except KeyError:
        print("chave não encontrada")
    except AttributeError:
        print("atributo não existe")
    except Exception as e:
        print(f"ocorreu um erro {e}")
    finally:
        print("finalizado")
        
    conexao.close()        

def alterar():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()
        id_atual = int(input("Digite o ID que deseja alterar: ")) 

        cursor.execute(f''' SELECT * FROM professor WHERE ID={id_atual}''')
        professor= cursor.fetchone()
        if not professor:
            print("professor não encontrado")
        else:    
            novo_nome = input("Novo nome: ")
            novo_telefone = input("Novo telefone: ") 
            cursor.execute(f'''UPDATE professor SET nome= '{novo_nome}', telefone='{novo_telefone}'
                    WHERE id= {id_atual} ''')  
        conexao.commit()
        print("Professor alterado com sucesso!")

    except ValueError:
        print("valor invalido")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except TypeError:
        print("erro de tipos de dados")
    except NameError:
        print("nome invalido")
    except IndexError:
        print("posição que não existe")
    except KeyError:
        print("chave não encontrada")
    except AttributeError:
        print("atributo não existe")
    except Exception as e:
        print(f"ocorreu um erro {e}")
    finally:
        print("finalizado")
    
    conexao.close()



def excluir():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()
        listar()
        id_professor = int(input("Digite o ID que deseja excluir: "))
        cursor.execute(f''' DELETE FROM  professor
                    WHERE id = {id_professor}''') 
        print("Professor excluido com sucesso! ")
        conexao.commit()
    
    except ValueError:
        print("valor invalido")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except TypeError:
        print("erro de tipos de dados")
    except NameError:
        print("nome invalido")
    except IndexError:
        print("posição que não existe")
    except KeyError:
        print("chave não encontrada")
    except AttributeError:
        print("atributo não existe")
    except Exception as e:
        print(f"ocorreu um erro {e}")
    finally:
        print("finalizado")

    conexao.close()

def menu ():
    try:
        while True:
            print("1-CADASTRAR | 2- LISTAR | 3- ALTERAR | 4- EXCLUIR | 5- SAIR ")
            opcao = input("Digite a opção: ")
            if opcao == "1" : criar_tabela()
            elif opcao =="2": listar()
            elif opcao =="3": alterar()
            elif opcao== "4": excluir()
            elif opcao == "5": break

    except ValueError:
        print("valor invalido")
    except sqlite3.IntegrityError:
        print("dados ja cadastrados")
    except TypeError:
        print("erro de tipos de dados")
    except NameError:
        print("nome invalido")
    except IndexError:
        print("posição que não existe")
    except KeyError:
        print("chave não encontrada")
    except AttributeError:
        print("atributo não existe")
    except Exception as e:
        print(f"ocorreu um erro {e}")


print("programa encerrado!")