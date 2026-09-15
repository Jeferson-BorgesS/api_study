from fastapi import FastAPI

app = FastAPI()

jogadores= {
    1: {"nome": "Cristiano Ronaldo", "idade": 38, "clube": "Al Nassr"},
    2: {"nome": "Lionel Messi", "idade": 36, "clube": "Inter Miami"},
    3: {"nome": "Neymar Jr", "idade": 31, "clube": "Santos"},
}

@app.get("/")
def inicio():
    return jogadores

@app.get("/get-jogador/{jogador_id}") # exemplo de Path parameter
def get_jogador(jogador_id: int):
    return jogadores.get(jogador_id)

# exemplo para Query parameter 
# @app.get("/get-jogador-query")
# def get_jogador_query(jogador_id: int):
#     return jogadores.get(jogador_id)
