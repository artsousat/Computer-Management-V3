from src.banco import conectar

conexao = conectar()

conexao.execute("""
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
""")

conexao.execute("""
    CREATE TABLE IF NOT EXISTS dispositivos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        estoque INTEGER NOT NULL CHECK (estoque >= 0),
        quebrados INTEGER NOT NULL CHECK (quebrados >= 0),
        sumido INTEGER NOT NULL CHECK (sumido >= 0),
        utilizaveis INTEGER NOT NULL CHECK (utilizaveis >= 0)
    )
""")

conexao.commit()

print("Banco de dados criado/autualizado com sucesso!")

conexao.close()