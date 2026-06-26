import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()
cursor.execute('''DROP TABLE alunos''')

conexao.close()


import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''ALTER TABLE alunos ADD COLUMN endereco TEXT''')

cursor.execute('''ALTER TABLE alunos ADD COLUMN cidade TEXT''')

cursor.execute('''ALTER TABLE alunos ADD COLUMN estado TEXT''')

conexao.close()


import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''ALTER TABLE professor ADD COLUMN endereco TEXT''')

cursor.execute('''ALTER TABLE professor ADD COLUMN cidade TEXT''')

cursor.execute('''ALTER TABLE professor ADD COLUMN estado TEXT''')

conexao.close()