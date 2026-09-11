import banco
import sqlite3

def cadastrar_escola(nome, cidade):
    conexao = sqlite3.connect('gestao_escoal.db')
    conexao.execute("PRAGMA foreign_keys = ON;")
    cursor = conexao.cursor()
    conexao = banco.conectar()
    
    assert nome() != "", "O nome da escola não pode ser vazio."
    assert cidade() != "", "A cidade da escola não pode ser vazia."
    
    cursor.execute("INSERT INTO escolas (nome, cidade) VALUES (?, ?);", (nome(), cidade()))
    conexao.commit()
    conexao.close()

def listar_escolas():
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM escolas;")
    escolas = cursor.fetchall()
    conexao.close()
    return escolas

def alterar_escola(id_escola, novo_nome, nova_cidade):
    assert id_escola > 0, "ID da escola inválido."
    assert novo_nome() != "", "O novo nome não pode ser vazio."
    assert nova_cidade() != "", "A nova cidade não pode ser vazia."
    
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE escolas SET nome = ?, cidade = ? WHERE id = ?;", (novo_nome(), nova_cidade(), id_escola))
    linhas_afetadas = cursor.rowcount
    conexao.commit()
    conexao.close()
    return linhas_afetadas > 0

def excluir_escola(id_escola):
    assert id_escola > 0, "ID da escola inválido."
    
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM escolas WHERE id = ?;", (id_escola,))
    linhas_afetadas = cursor.rowcount
    conexao.commit()
    conexao.close()
    return linhas_afetadas > 0