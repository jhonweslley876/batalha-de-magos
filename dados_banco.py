import sqlite3

def conectar():
    return sqlite3.connect('escola.db')

def criar_tabela():
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos(
        nome TEXT NOT NULL PRIMARY KEY,
        senha TEXT NOT NULL)
    ''')

    conexão.commit()
    conexão.close()

def inserir(nome, idade, curso):
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('INSERT INTO alunos(nome, idade, curso) VALUES(?,?,?)', (nome, idade, curso))
    conexão.commit()
    conexão.close()

def listar():
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('SELECT * FROM alunos')
    for linha in cursor.fetchall():
        print(linha)
    conexão.close()

def atualizar(id, nome, idade, curso):
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('UPDATE alunos SET nome=?, idade=?, curso=? Where id=?',  (nome, idade, curso, id))
    conexão.commit()
    conexão.close()

def excluir(id):
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('DELETE FROM alunos WHERE id=?', (id,))
    conexão.commit()
    conexão.close()

criar_tabela()

def login():
    print('┌───┬─────────┬───┬─────────────┐')
    print('│ 1 │  LOGIN  │ 2 │ CRIAR CONTA │')
    print('└───┴─────────┴───┴─────────────┘')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
