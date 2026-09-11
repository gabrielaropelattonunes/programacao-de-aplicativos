import banco
import sqlite3

def cadastrar_turma(nome_turma, id_escola):
    conexao = sqlite3.connect('gestao_escoal.db')
    conexao.execute("PRAGMA foreign_keys = ON;")
    cursor = conexao.cursor()
    conexao = banco.conectar()

    
    assert nome_turma() != "", "O nome da turma não pode ser vazio."
    assert id_escola > 0, "O ID da escola deve ser maior que zero."
    
    cursor.execute("INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?);", (nome_turma(), id_escola))
    conexao.commit()
    conexao.close()

def listar_turmas():
    conexao = sqlite3.connect('gestao_escoal.db')
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM turmas;")
    turmas = cursor.fetchall()
    conexao.close()
    return turmas

def alterar_turma(id_turma, novo_nome, novo_id_escola):
    conexao = sqlite3.connect('gestao_escoal.db')
    cursor = conexao.cursor()
    
    assert id_turma > 0, "ID da turma inválido."
    assert novo_nome() != "", "O novo nome da turma não pode ser vazio."
    assert novo_id_escola > 0, "O ID da escola deve ser maior que zero."
    
    
    cursor.execute("UPDATE turmas SET nome_turma = ?, id_escola = ? WHERE id = ?;", (novo_nome(), novo_id_escola, id_turma))
    linhas_afetadas = cursor.rowcount
    conexao.commit()
    conexao.close()
    return linhas_afetadas > 0

def excluir_turma(id_turma):
    conexao = sqlite3.connect('gestao_escoal.db')
    cursor = conexao.cursor()

    assert id_turma > 0, "ID da turma inválido."
    
    cursor.execute("DELETE FROM turmas WHERE id = ?;", (id_turma,))
    linhas_afetadas = cursor.rowcount
    conexao.commit()
    conexao.close()
    return linhas_afetadas > 0