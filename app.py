from fastapi import FastAPI, Query
import json

app = FastAPI()

def baixar_permissoes():
    with open("permissoes.json", "r", encoding="utf-8") as file_permissoes:
        return json.load(file_permissoes)

@app.get("/api/verificar_acesso/")
def validar_acesso_usuario(nome: str = Query(...), lugar_acesso: str = Query(...)):
    permissoes = baixar_permissoes()

    for usuario in permissoes["usuarios"]:
        if usuario["nome"].lower() == nome.lower():
            if lugar_acesso.lower() in map(str.lower, usuario["acessos"]):
                mensagem = "✅ Acesso permitido!"
                return {mensagem}
            else:
                mensagem = "❌ Acesso negado!"
                return {mensagem}
        else:
            return "O usuário não foi encontrado, tente novamente!"
