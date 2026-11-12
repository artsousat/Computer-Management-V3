import sqlite3
from pathlib import Path

def conectar():
    pasta_projeto = Path(__file__).resolve().parent.parent
    caminho_banco = pasta_projeto / "dados" / "computer_management.db"
    return sqlite3.connect(caminho_banco)