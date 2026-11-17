import json
from pathlib import Path
from src.banco import conectar

pasta_projeto = Path(__file__).resolve().parent 
caminho_professores_json = pasta_projeto / "dados" / "professores.json"
caminho_dispositivos_json = pasta_projeto / "dados" / "dispositivos.json"

with open(caminho_professores_json, "r", encoding="utf-8") as arquivo:
    professores = json.load(arquivo)

with open(caminho_dispositivos_json, "r", encoding="utf-8") as arquivo:
    dispositivos = json.load(arquivo)

conexao = conectar()

for numero, professor in professores.items():
    conexao.execute("INSERT INTO professores (id, nome) VALUES (?, ?)", (int(numero), professor))

for numero, dispositivo in dispositivos.items():
    conexao.execute("INSERT INTO dispositivos (id, nome, estoque, quebrados, sumido, utilizaveis) VALUES (?, ?, ?, ?, ?, ?)", 
                    (int(numero), dispositivo["nome"], dispositivo["estoque"], dispositivo["quebrados"], dispositivo["sumido"], dispositivo["utilizaveis"]))

conexao.commit()
conexao.close()

print("Dados importados com sucesso!")