from fastapi import FastAPI, Query
import json

app = FastAPI()

def baixar_permissoes():
    with open("permissoes.json", "r", encoding="utf-8") as file_permissoes:
        return json.load(file_permissoes)
