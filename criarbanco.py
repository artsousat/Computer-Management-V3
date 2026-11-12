from src.banco import conectar

conexao = conectar()

conexao.execute("""
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
""")

conexao.commit()

resultado = conexao.execute("SELECT id, nome FROM professores")

professores = resultado.fetchall()

print(professores)

conexao.close()