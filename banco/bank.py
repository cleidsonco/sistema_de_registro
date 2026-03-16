import sqlite3

def criar_banco():
    conn = sqlite3.connect('registros.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            nome TEXT,
                                            email TEXT,
                                            telefone TEXT,
                                            preco REAL,
                                            servicos TEXT,
                                            detalhes TEXT)''')

    conn.commit()                                      
    conn.close()

def conectar():
    return sqlite3.connect('registros.db')


def adicionar(nome, email, telefone, preco, servicos, detalhes):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(''' INSERT INTO registros (nome, email, telefone, preco, servicos, detalhes)
                VALUES (?,?,?,?,?,?)''',
                (nome, email, telefone, preco, servicos, detalhes))
    
    conn.commit()
    conn.close()

def ver():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM registros")

    dados =  cursor.fetchall()

    for id, nome, email, telefone, preco, servicos, detalhes in dados:
        print(f"ID:{id} | Nome:{nome} | Serviço:{servicos} | Preço:{preco}")
    
    conn.close()


def editar(id, nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
                UPDATE registros
                SET nome = ?
                WHERE id = ?
                ''', (nome, id))
    conn.commit()
    conn.close()


def excluir(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM registros WHERE id = ?", (id,))

    conn.commit()
    conn.close()
