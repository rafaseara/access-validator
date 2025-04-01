from fastapi import FastAPI, Query
import json
import os

app = FastAPI()

def baixar_permissoes():
    try:
        with open("permissoes.json", "r", encoding="utf-8") as file_permissoes:
            return json.load(file_permissoes)
    except FileNotFoundError:
        return {"mensagem": "Arquivo de permissões não encontrado!"}
    except json.JSONDecodeError:
        return {"mensagem": "Erro ao processar o arquivo de permissões!"}

@app.get("/api/verificar_acesso/")
def validar_acesso_usuario(nome: str = Query(...), lugar_acesso: str = Query(...)):
    permissoes = baixar_permissoes()

    for usuario in permissoes["usuarios"]:
        if usuario["nome"].lower() == nome.lower():
            if lugar_acesso.lower() in map(str.lower, usuario["acessos"]):
                return {"mensagem": "✅ Acesso permitido!"}
            else:
                return {"mensagem": "❌ Acesso negado!"}
    return {"mensagem": "O usuário não foi encontrado, tente novamente!"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)