from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

jogadores= {
    1: {"nome": "Cristiano Ronaldo", "idade": 38, "clube": "Al Nassr"},
    2: {"nome": "Lionel Messi", "idade": 36, "clube": "Inter Miami"},
    3: {"nome": "Neymar Jr", "idade": 31, "clube": "Santos"},
}

class Jogador(BaseModel):
    nome: str
    idade: int
    clube: str

@app.get("/")
def inicio():
    return jogadores

@app.get("/get-jogador/{jogador_id}") # exemplo de Path parameter
def get_jogador(jogador_id: int):
    return jogadores[jogador_id]

@app.get("/get-jogador-time")
def get_jogador_time(clube: str):
    for jogador_id in jogadores:
        if jogadores[jogador_id]["clube"] == clube:
            return jogadores[jogador_id]

    return {"Info": "Nenhum jogador encontrado para o clube informado."}
# API Métodos
@app.get("/")
def inicio():
    return jogadores

@app.post("/cadastrar-jogador/{jogador_id}")
def cadastrar_jogador(jogador_id: int, jogador: Jogador):
    if jogador_id <= 0:
            return {"Info": "ID do jogador deve ser maior que zero."}

    if jogador_id in jogadores:
        return {"Info": "ID do jogador já cadastrado."}

    jogadores[jogador_id] = jogador
    return jogadores[jogador_id]

@app.delete("/deletar-jogador/{jogador_id}")
def deletar_jogador(jogador_id: int):
    if jogador_id in jogadores:
        del jogadores[jogador_id]
        return {"Info": "Jogador deletado com sucesso."}
    else:
        return {"Info": "ID do jogador não encontrado."}

@app.put("/atualizar-jogador/{jogador_id}")
def atualizar_jogador(jogador_id: int, jogador: Jogador):
    if jogador_id in jogadores:
        jogadores[jogador_id] = jogador
        return jogadores[jogador_id]
    else:
        return {"Info": "ID do jogador não encontrado."}