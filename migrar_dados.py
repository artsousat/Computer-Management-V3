import json
from pathlib import Path
from src.banco import conectar

pasta_projeto = Path(__file__).resolve().parent 
caminho_json = pasta_projeto / "dados" / "professores.json"

with open(caminho_json, "r", encoding="utf-8") as arquivo:
    professores = json.load(arquivo)

conexao = conectar()

for numero, professor in professores.items():
    conexao.execute("INSERT INTO professores (id, nome) VALUES (?, ?)", (int(numero), professor))

conexao.commit()
conexao.close()
